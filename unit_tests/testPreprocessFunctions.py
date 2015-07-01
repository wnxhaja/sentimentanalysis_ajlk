__author__ = 'kert'

import unittest, sys, os

PARENT_DIR = os.path.dirname(os.path.abspath(os.getcwd()))
sys.path.append(PARENT_DIR)

from preprocess import Preprocess

class TestPreprocessFunctions(unittest.TestCase):

	def setUp(self):
		self.p = Preprocess("Won't be sleeping for an #overnight with @meyaan. This is going to be a looooooooooooooong night :( #thesis")


	def testToLowerCase(self):
		result = self.p.toLowerCase()
		expected = "won't be sleeping for an #overnight with @meyaan. this is going to be a looooooooooooooong night " \
		           ":( #thesis
		self.assertEquals(result, expected)

	def testRemoveMentions(self):
		result = self.p.removeMentions()
		expected = "won't be sleeping for an #overnight with . this is going to be a looooooooooooooong night " \
		           ":( #thesis
		self.assertEquals(result, expected)

	def testRemoveHashtags(self):
		result = self.p.removeHashtags()
		expected = "won't be sleeping for an overnight with . this is going to be a looooooooooooooong night " \
		           ":( thesis
		self.assertEquals(result, expected)

	def testRemoveURLs(self):
		pass

	def removeStopWords(self):
		expected = "won't be sleeping for an overnight with . this is going to be a looooooooooooooong night " \
		           ":( thesis

	def testTruncateElongatedWords(self):
		pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPreprocess))
unittest.TextTestRunner(verbosity=2).run(suite)