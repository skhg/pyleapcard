#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from . import CardEvent
from . import CardOverview
import re

class LeapSession:

    def __init__(self):
        self.__non_decimal = re.compile(r'[^\d.-]+')

        self.leap_website_url = "https://www.leapcard.ie"
        self.__session = requests.session()

        headers = {'Connection': 'keep-alive',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'User-agent': 'Mozilla/5.0 (comptabile)'}

        self.__session.headers = headers

    def login_url(self):
        return self.leap_website_url+"/en/login.aspx"

    def __handle_login_response(self, login_result, user):
        expectedLoginString = "<span id=\"LoginName1\">"+user+"</span>"
        if expectedLoginString.encode() in login_result.content:
            return True
        elif "Your credentials are incorrect." in login_result.content:
            raise IOError("Your credentials are incorrect.")
        else:
            raise IOError("Unknown error.")

    def try_login(self, user, passwd):
        
        login_send_url = self.login_url()
        try:
            login_form_response = self.__session.get(login_send_url)
            soup = BeautifulSoup(login_form_response.content,"html.parser")

            VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
            VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
            EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']
            EVENTTARGET = soup.find(id="__EVENTTARGET")['value']
            EVENTARGUMENT = soup.find(id="__EVENTARGUMENT")['value']
            SCROLLPOSITIONX = soup.find(id="__SCROLLPOSITIONX")['value']
            SCROLLPOSITIONY = soup.find(id="__SCROLLPOSITIONY")['value']
            VIEWSTATEENCRYPTED = soup.find(id="__VIEWSTATEENCRYPTED")['value']
            PREVIOUSPAGE = soup.find(id="__PREVIOUSPAGE")['value']

            login_details = {"__VIEWSTATE":VIEWSTATE,
                         "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
                         "__EVENTVALIDATION":EVENTVALIDATION,
                         "__EVENTTARGET":EVENTTARGET,
                         "__EVENTARGUMENT":EVENTARGUMENT,
                         "__SCROLLPOSITIONX":SCROLLPOSITIONX,
                         "__SCROLLPOSITIONY":SCROLLPOSITIONY,
                         "__VIEWSTATEENCRYPTED":VIEWSTATEENCRYPTED,
                         "__PREVIOUSPAGE":PREVIOUSPAGE,
                         'ctl00$ContentPlaceHolder1$UserName' : user,
                         'ctl00$ContentPlaceHolder1$Password' : passwd,
                         'ctl00$ContentPlaceHolder1$btnlogin' : "Login",
                         'AjaxScriptManager_HiddenField'      : '',
                         '_URLLocalization_Var001'            : False }
            
            login_response= self.__session.post(login_send_url, data = login_details)
            return self.__handle_login_response(login_response, user)

        except requests.exceptions.ConnectionError:
            # The most likely failure case is that we're offline so fail gracefully here
            return False

    def __get_standard_overview_field_by_name(self, overview_soup, field_name):
        field_label = overview_soup.find(text=field_name)
        field_row = field_label.parent.parent.parent
        field_value = field_row.select("div")[1].get_text(strip=True)
        return field_value

    def get_card_overview(self):
        card_overview_url = self.leap_website_url+"/en/SelfServices/CardServices/CardOverView.aspx"
        overview_page = self.__session.get(card_overview_url)
        overview_soup = BeautifulSoup(overview_page.content,"html.parser")
        
        balance_label = overview_soup.find(text="Travel Credit Balance (€)")
        balance_row = balance_label.parent.parent.parent
        balance_cell = balance_row.findChild("div",{"class":"pull-left"})
        current_balance = float(balance_cell.text)
        
        card_number = self.__get_standard_overview_field_by_name(overview_soup, "Card Number")
        card_type = self.__get_standard_overview_field_by_name(overview_soup, "Card Type")
        card_status = self.__get_standard_overview_field_by_name(overview_soup, "Card Status")
        credit_status = self.__get_standard_overview_field_by_name(overview_soup, "Travel Credit Status")
        auto_topup = self.__get_standard_overview_field_by_name(overview_soup, "Auto Top-Up")
        issue_date = self.__get_standard_overview_field_by_name(overview_soup, "Card Issue Date")
        expiry_date = self.__get_standard_overview_field_by_name(overview_soup, "Card Expiry Date")

        cardname_label = overview_soup.find(text="Card Label")
        cardname_row = cardname_label.parent.parent.parent
        cardname_row.select("div")[1].select("span")[0].decompose() #delete a messy <span> tag
        card_name = cardname_row.select("div")[1].get_text(strip=True)
        
        return CardOverview(card_number, card_name, current_balance, card_type, card_status, credit_status, auto_topup, issue_date, expiry_date)

    def __extract_event_details__(self, journeys_table):
        events = []

        journey_rows = journeys_table.select("tr")
        journey_rows.pop(0) #remove first row- header

        journey_rows.pop(len(journey_rows)-1)
        journey_rows.pop(len(journey_rows)-1) # remove last 2 rows - just links
        
        for row in journey_rows:
            cells = row.select("td")
            
            j_date = cells[0].get_text()
            j_time = cells[1].get_text()
            
            j_provider = cells[2].get_text(strip=True)
            
            j_valueAsString = cells[4].get_text()
            j_value = float(self.__non_decimal.sub('', j_valueAsString))
            
            j_event_type = cells[3].get_text(strip=True)
                    
            was_topup = False
            
            if "Top-Up" in j_event_type:
                was_topup = True
            
            events.append(CardEvent(j_date, j_time, j_provider, j_value, j_event_type, was_topup))
            
        return events

    def get_events(self):
        journey_history_url = self.leap_website_url+"/en/SelfServices/CardServices/ViewJourneyHistory.aspx"
        journeys_page = self.__session.get(journey_history_url)
        journeys_soup = BeautifulSoup(journeys_page.content,"html.parser")
        
        journeys_table = journeys_soup.find(id="gvCardJourney")
        return self.__extract_event_details__(journeys_table)