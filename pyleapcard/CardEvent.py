#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CardEvent:
    
    def __init__(self, date, time, provider, price, was_topup):
        self.date = date
        self.time = time
        self.provider = provider
        self.price = price
        self.was_topup = was_topup