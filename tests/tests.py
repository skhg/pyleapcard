import unittest
from unittest import TestCase
import pickle
import sys
import pyleapcard
import json
from pyleapcard import *

pickledir = ""
if sys.version_info[0] < 3:
	pickledir = "./tests/sampledata/2.7/"
else:
	pickledir = "./tests/sampledata/3.6/"

class TestLoginMethod(unittest.TestCase):

	def test_handle_login_response_good_response_returns_true(self):
		session = LeapSession()

		with(open(pickledir+"login_result.dat", "rb")) as f:
			good_login = pickle.load(f)

			loginOk = session._LeapSession__handle_login_response(good_login,'usernam')

			self.assertTrue(loginOk)

	def test_handle_login_response_wrong_credentials_throws(self):
		session = LeapSession()

		with(open(pickledir+"failed_login_result.dat", "rb")) as f:
			failed_login = pickle.load(f)

			with self.assertRaises(IOError) as context:
				session._LeapSession__handle_login_response(failed_login,'usernam')

			self.assertTrue('Your credentials are incorrect' in str(context.exception))


class TestOverviewMethod(unittest.TestCase):

	def test_calls_overview_returns_expected(self):
		session = LeapSession()

		with(open(pickledir+"overview_page.dat", "rb")) as f:
			page = pickle.load(f)
			result = session._LeapSession__handle_card_overview_response(page)

			expected = CardOverview(u"1000000000", u"User's Card", 25.02, u"Adult", u"Unblocked", u"Unblocked", u"Not Enabled", u"02/04/2012 12:00:00 AM", u"09/12/2023 12:00:00 AM")

			self.assertEqual(result.__dict__,expected.__dict__)


class TestEventsMethod(unittest.TestCase):

	def test_calls_events_returns_expected(self):
		session = LeapSession()

		with(open(pickledir+"journeys_page.dat", "rb")) as f:
			page = pickle.load(f)
			result = session._LeapSession__handle_events_response(page)
			
			resultStr = ""
			for item in result:
				resultStr+=str(item.__dict__)

			expected = ""
			if sys.version_info[0] < 3:
				expected = "{'event_type': u'Travel Credit Deduction', 'price': -2.64, 'time': u'9:11 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'17/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -2.64, 'time': u'5:37 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'17/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'10:28 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'15/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'12:46 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'15/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'6:47 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'09/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'5:40 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'08/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'4:18 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'06/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'11:45 AM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'06/09/2017'}{'event_type': u'Travel Credit Top-Up', 'price': 50.0, 'time': u'10:00 AM', 'was_topup': True, 'provider': u'Leap Top-Up App', 'date': u'06/09/2017'}{'event_type': u'Travel Credit Deduction', 'price': -3.52, 'time': u'12:16 PM', 'was_topup': False, 'provider': u'Bus Eireann', 'date': u'02/09/2017'}"
			else:
				expected = "{'date': '17/09/2017', 'time': '9:11 PM', 'provider': 'Bus Eireann', 'price': -2.64, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '17/09/2017', 'time': '5:37 PM', 'provider': 'Bus Eireann', 'price': -2.64, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '15/09/2017', 'time': '10:28 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '15/09/2017', 'time': '12:46 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '09/09/2017', 'time': '6:47 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '08/09/2017', 'time': '5:40 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '06/09/2017', 'time': '4:18 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '06/09/2017', 'time': '11:45 AM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '06/09/2017', 'time': '10:00 AM', 'provider': 'Leap Top-Up App', 'price': 50.0, 'event_type': 'Travel Credit Top-Up', 'was_topup': True}{'date': '02/09/2017', 'time': '12:16 PM', 'provider': 'Bus Eireann', 'price': -3.52, 'event_type': 'Travel Credit Deduction', 'was_topup': False}"

			self.assertEqual(resultStr, expected)


if __name__ == '__main__':
	unittest.main()