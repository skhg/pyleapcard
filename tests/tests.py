import unittest
from pyleapcard import LeapSession, CardOverview

sampledatadir = "./tests/sampledata/"


class TestLoginMethod(unittest.TestCase):

    def test_handle_login_response_good_response_returns_true(self):
        session = LeapSession()

        with(open(sampledatadir + "login_result.html", "rb")) as f:
            good_login = f.read()

            loginOk = session._LeapSession__handle_login_response(good_login, 'usernam')

            self.assertTrue(loginOk)

    def test_handle_login_response_wrong_credentials_throws(self):
        session = LeapSession()

        with(open(sampledatadir + "failed_login_result.html", "rb")) as f:
            failed_login = f.read()

            with self.assertRaises(IOError) as context:
                session._LeapSession__handle_login_response(failed_login, 'usernam')

            self.assertTrue('Your credentials are incorrect' in str(context.exception))


class TestOverviewMethod(unittest.TestCase):

    def test_calls_overview_returns_expected(self):
        session = LeapSession()

        with(open(sampledatadir + "overview_page.html", "r")) as f:
            page = f.read()
            result = session._LeapSession__handle_card_overview_response(page)

            expected = CardOverview(u"1000000000", u"User's Card", 25.02, u"Adult", u"Unblocked", u"Unblocked",
                                    u"Not Enabled", u"02/04/2012 12:00:00 AM", u"09/12/2023 12:00:00 AM")

            self.assertEqual(result.__dict__, expected.__dict__)


class TestEventsMethod(unittest.TestCase):

    def test_calls_events_returns_expected(self):
        session = LeapSession()

        with(open(sampledatadir + "journeys_page.html", "r")) as f:
            page = f.read()
            result = session._LeapSession__handle_events_response(page)

            resultStr = ""
            for item in result:
                resultStr += str(item.__dict__)

            expected = "{'date': '11/02/2020', 'time': '6:02 PM', 'provider': 'Bus Eireann', 'price': -1.96, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '08/02/2020', 'time': '8:30 PM', 'provider': 'Bus Eireann', 'price': -1.96, 'event_type': 'Travel Credit Deduction', 'was_topup': False}{'date': '08/02/2020', 'time': '12:50 PM', 'provider': 'Leap Top-Up App', 'price': 20.0, 'event_type': 'Travel Credit Top-Up', 'was_topup': True}{'date': '05/07/2019', 'time': '6:22 PM', 'provider': 'Bus Eireann', 'price': -1.96, 'event_type': 'Travel Credit Deduction', 'was_topup': False}"

            self.assertEqual(resultStr, expected)


if __name__ == '__main__':
    unittest.main()
