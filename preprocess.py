import re
from stopwords import StopWords

class Preprocess:

	def __init__(self, text):
		self.text = text
		self.stopWords = StopWords()

	def preprocess(self):
		pass
		#self.segment()
		#self.toLowerCase()
		#self.removeMentions()
		#self.handleHashTags()
		#self.completContractions()
		#self.truncateElongatedWords()


		return []

	def segmentText(self):
		pass

	def truncateElongatedWords(self, word):
		pass

	def

	def toLowerCase(self):
		self.text.lower()
