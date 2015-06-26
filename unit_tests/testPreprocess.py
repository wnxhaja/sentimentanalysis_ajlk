import unittest#, os, sys

#sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "../")
#from preprocess import Preprocess

execfile("../preprocess.py", globals())
class TestPreprocess(unittest.TestCase):

	def setUp(self):
		#print(sys)
		tweet = "hello"
		self.prep = Preprocess(tweet)

	def testPrintTweet(self):
		self.assertEqual(self.prep.printTweet(), "hello")

	def testTweetWithElongatedWords(self):
		tweet = "Huuuraaaaay so haaaaaapppppppppyyyyyyyy for today"
		result = self.prep.truncateElongatedWords(tweet)
		expected = "Huuraay so haappyy for today"
		self.assertEqual(expected, result)

	def testTweetWithContractions(self):
		pass

	def testTweetWithMentions(self):
		pass

	def testTweetWithURL(self):
		pass

	def testTweetWithHashtagNotEnd(self):
		pass

	def testTweetWithHashtagEnd(self):
		pass

	def testTweetSegmentation(self):
		pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPreprocess))
unittest.TextTestRunner(verbosity=2).run(suite)
