import re

class Preprocess:

	def __init__(self, tweet):
		self.tweet = tweet


	def printTweet(self):
		return self.tweet

	def preprocessTweet(self):
		pass


	#helper functions
	def truncateElongatedWords(self, word):
		return ""