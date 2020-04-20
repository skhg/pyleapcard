# pyleapcard
[![Build Status](https://travis-ci.org/skhg/pyleapcard.svg?branch=master)](https://travis-ci.org/skhg/pyleapcard) [![PyPI](https://img.shields.io/pypi/v/pyleapcard.svg)](https://pypi.python.org/pypi/pyleapcard/) [![codecov](https://codecov.io/gh/skhg/pyleapcard/branch/master/graph/badge.svg)](https://codecov.io/gh/skhg/pyleapcard)

A Python API for accessing your current card balance and stats for Ireland's public transport [Leap Card](https://www.leapcard.ie/). This is an unoffical API and the author/contributors are in no way connected to Leap Card, Transport for Ireland, or any other agency. The API provides methods to:
* Get your credit balance and card status information
* Get a list of your recent trips & topups

For an example of this in use, see my [Leap Card BitBar plugin](https://github.com/skhg/BitBar-Plugins/tree/master/LeapCard)

## Installation
`pip install pyleapcard`

## Usage
It's very easy to use. Try the following to get your card status and current balance:
```python
from pyleapcard import *
from pprint import pprint

session = LeapSession()
session.try_login("<username>","<password>")

overview = session.get_card_overview()
pprint(vars(overview))
```
returns:
```python
{'auto_topup': u'Not Enabled',
 'balance': 25.02,
 'card_label': u"<Card Label>",
 'card_num': u'<Card Number>',
 'card_status': u'Unblocked',
 'card_type': u'Adult',
 'credit_status': u'Unblocked',
 'expiry_date': u'09/12/2023 12:00:00 AM',
 'issue_date': u'02/04/2012 12:00:00 AM'}
 ```
 
 Or to get your recent trips/topups add the following:
 ```python
 events = session.get_events()
for item in events:
	pprint(vars(item))
  ```
  returns:
  ```python
  {'date': u'06/09/2017',
 'event_type': u'Travel Credit Deduction',
 'price': -3.52,
 'provider': u'Bus Eireann',
 'time': u'11:45 AM',
 'was_topup': False}
{'date': u'06/09/2017',
 'event_type': u'Travel Credit Top-Up',
 'price': 50.0,
 'provider': u'Leap Top-Up App',
 'time': u'10:00 AM',
 'was_topup': True}
{'date': u'02/09/2017',
 'event_type': u'Travel Credit Deduction',
 'price': -3.52,
 'provider': u'Bus Eireann',
 'time': u'12:16 PM',
 'was_topup': False}
 ```
 
 ## Tests
 `python ./tests/tests.py`
 
 ## Contributing
 Fork this repo, make some changes and create a new pull request!
