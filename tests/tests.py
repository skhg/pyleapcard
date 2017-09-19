import unittest
from unittest import TestCase
import pickle

import pyleapcard
from pyleapcard import LeapSession

class TestStringMethods(unittest.TestCase):

	def test_handle_login_response_good_response_returns_true(self):
		session = LeapSession()
		good_login = pickle.load(open("./tests/sampledata/login_result.dat", "rb"))

		loginOk = session._LeapSession__handle_login_response(good_login,'username')

		self.assertTrue(loginOk)

	def test_handle_login_response_wrong_credentials_throws(self):
		session = LeapSession()
		failed_login = pickle.load(open("./tests/sampledata/failed_login_result.dat", "rb"))

		with self.assertRaises(IOError) as context:
			session._LeapSession__handle_login_response(failed_login,'username')

		self.assertTrue('Your credentials are incorrect' in str(context.exception))

if __name__ == '__main__':
	unittest.main()