#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CardOverview:
        
    def __init__(self, card_num, card_name, balance):
        self.__card_num = card_num
        self.__card_name = card_name
        self.__balance = balance
        
    def card_info(self):
        return self.__card_num+" (" + self.__card_name + ")"
    
    def card_name(self):
        return self.__card_name

    def card_number(self):
        return self.__card_num
        
    def balance(self):
        balance_string =u""
        negative_balance = False

        if self.__balance < 0:
            balance_string = u"- "
            negative_balance = True

        balance_string += u"€"+str(abs(self.__balance))

        if negative_balance:
            balance_string += " | color=orange"
        
        return balance_string