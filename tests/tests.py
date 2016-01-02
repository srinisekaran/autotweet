import unittest
from tweet import add_content, get_status
import config

class AutoTweetTest(unittest.TestCase):

	def test_add_content(self):
		content_to_list = ('tweet.py This is a test.').split() # tweet.py is the first argument and is ignored
		self.assertIsNone(add_content(content_to_list))

	def test_get_status(self):
		self.assertEqual(get_status(), 'This is a test.')

if __name__ == '__main__':
	unittest.main()