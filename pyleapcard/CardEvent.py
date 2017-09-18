#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CardEvent:
    
    def __init__(self, date, time, provider, price, was_topup):
        self.__date = date
        self.__time = time
        self.__provider = provider
        self.__price = price
        self.__was_topup = was_topup
    
    def to_str(self):
        styleInfo = " | font=Courier"
        
        if self.__was_topup is True:
            styleInfo += " color=green"
        
        return u""+self.__date + " " + self.__time + " (" + self.__provider + ") "+ self.__price+styleInfo
