import unittest, sys, os

PARENT_DIR = os.path.dirname(os.path.abspath(os.getcwd()))
sys.path.append(PARENT_DIR)

#execfile("../preprocess.py", global())
from preprocess import Preprocess

class TestPreprocess(unittest.TestCase):

	def testPreprocessNormalTweet(self):
		tweet = "Thinking trying social media management tool? Test drive Sprout Social free today!"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["thinking trying social media management tool", []], ["test drive sprout social free today", []]]
		self.assertEqual(result, expected)

	def testPreprocessTweetWithMidHashtag(self):
		tweet = "New always-on #AndroidWear apps keep info handy for when you are on the go"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["new always-on androidwear apps keep info handy when go", []]]
		self.assertEqual(result, expected)

	def testPreprocessTweetWithEndHashtag(self):
		tweet = "THANKS FOR ALL THE QUESTIONS DURING THIS GAB! KEEP VOTING USING #ChoiceSciFiTVActress"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["thanks questions during gab", []], ["keep voting using", []]]
		self.assertEqual(result, expected)


	def testPreprocessWithEmoticons(self):
		tweet = "dili kaayu klaro imuha :( HAHAHAHA haaays! dapat ipa zoom ang nawong pa more HAHAHAHA :P"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["dili kaayo klaro imuha", [":("]], ["hahahaha haays", []] ["dapat ipa zoom ang nawong pa more "
		                                                                        "hahahaha", [":P"]]]
		self.assertEqual(result, expected)

	def testPreprocessWithMentions(self):
		tweet = "Take a trip to Central City with @MiloVentimiglia and The PET Squad"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["take trip central city pet squad", []]]
		self.assertEqual(result, expected)

	def testPreprocessWithContractions(self):
		tweet = "this isn't real! :("
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["real", []], ["", [":("]]]
		self.assertEqual(result, expected)

	def testPreprocessWithElongatedWords(self):
		tweet = "dili kaayu klaro imuha :( HAHAHAHA haaaaaaaaaaaaaaays! dapat ipa zoom ang nawong pa more HAHAHAHA :P"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["dili kaayo klaro imuha", [":("]], ["hahahaha haays", []]["dapat ipa zoom ang nawong pa more "
		                                                                       "hahahaha", [":P"]]]
		self.assertEqual(result, expected)

	def testPreprocessWithAllCases(self):
		#edit it
		tweet = "Won't be sleeping for an #overnight with @meyaan. This is going to be a looooooooooooooong night :( #thesis"
		prep = Preprocess(tweet)
		result = prep.preprocess()
		expected = [["sleeping overnight", []], ["going loong night", [":("]]]
		self.assertEqual(result, expected)



suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPreprocess))
unittest.TextTestRunner(verbosity=2).run(suite)
