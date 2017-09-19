#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CardOverview:
        
    def __init__(self, card_num, card_label, balance, card_type, card_status, credit_status, auto_topup, issue_date, expiry_date):
        self.card_num = card_num
        self.card_label = card_label
        self.balance = balance
        self.card_type = card_type
        self.card_status = card_status
        self.credit_status = credit_status
        self.auto_topup = auto_topup
        self.issue_date = issue_date
        self.expiry_date = expiry_date
