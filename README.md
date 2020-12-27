# pyleapcard
[![PyPI](https://img.shields.io/pypi/v/pyleapcard.svg)](https://pypi.python.org/pypi/pyleapcard/) [![codecov](https://codecov.io/gh/skhg/pyleapcard/branch/master/graph/badge.svg)](https://codecov.io/gh/skhg/pyleapcard) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pyleapcard)

## Login Flow bug (December 2020)
As of December 2020, the login flow has changed, to use a Microsoft Azure SSO provider. This has broken the old login flow, so this library currently does not work. See [issue 20](https://github.com/skhg/pyleapcard/issues/20) for details. If anyone can suggest a fix, it would be appreciated.

## About
A Python API for accessing your current card balance and stats for Ireland's public transport [Leap Card](https://www.leapcard.ie/). This is an unoffical API and the author/contributors are in no way connected to Leap Card, Transport for Ireland, or any other agency. The API provides methods to:
* Get your credit balance and card status information
* Get a list of your recent trips & topups

For an example of this in use, see my [Leap Card BitBar plugin](https://github.com/skhg/BitBar-Plugins/tree/master/LeapCard)

## Prerequisites
You need a [TfI](https://www.transportforireland.ie/) ID which you can use to login to a working [leapcard.ie](https://www.leapcard.ie/) account. You also need at least one active Leap Card associated with your account, in order to be able to get any useful data. Before using this library, please verify that you can log in successfully to your Leap Card account using your web browser.

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
 
## Troubleshooting
This library attempts to give helpful error messages, but can't cover all cases. If something isn't working, the first step is usually to use your browser to ensure that you can login to the Leap Card website manually using the same credentials. If this works, then it might be the case that the Leap Card website itself has changed, and the web scraping code in this library no longer works. This is likely to occur over time as the website is updated.

If you wish, you can report an issue with details of the problem, what you've tried to do to fix it, and your intuition on what might be the root cause.
 
 ## Contributing
 Fork this repo, make some changes and create a new pull request! All contributions and shared efforts are appreciated.
