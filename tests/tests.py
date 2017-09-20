import unittest
from unittest import TestCase
import pickle
import sys
import pyleapcard
from pyleapcard import LeapSession

class TestStringMethods(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		if sys.version_info[0] < 3:
			self.__pickledir = "./tests/sampledata/2.7/"
		else:
			self.__pickledir = "./tests/sampledata/3.6/"

		super(TestStringMethods, self).__init__(*args, **kwargs)

	def test_handle_login_response_good_response_returns_true(self):
		session = LeapSession()

		with(open(self.__pickledir+"login_result.dat", "rb")) as f:
			good_login = pickle.load(f)

			loginOk = session._LeapSession__handle_login_response(good_login,'usernam')

			self.assertTrue(loginOk)

	def test_handle_login_response_wrong_credentials_throws(self):
		session = LeapSession()

		with(open(self.__pickledir+"failed_login_result.dat", "rb")) as f:
			failed_login = pickle.load(f)

			with self.assertRaises(IOError) as context:
				session._LeapSession__handle_login_response(failed_login,'usernam')

			self.assertTrue('Your credentials are incorrect' in str(context.exception))

if __name__ == '__main__':
	unittest.main()