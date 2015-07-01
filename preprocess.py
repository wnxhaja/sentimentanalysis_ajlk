import re
from stopwords import StopWords

class Preprocess:

	def __init__(self, text):
		self.text = text
		self.stopWords = StopWords()
		#self.repeatingCharactersPattern = r'(.)\1{2,}'

	#returns a list
	def preprocess(self):
		pass

	def segmentText(self):
		pass

	def truncateElongatedWords(self):
		self.text = re.sub(r'(.)\1{2,}', r'\1\1', self.text)

	def removeMentions(self):
		self.text = re.sub(r'@(\w+)', r'', self.text)

	#hashtags end sa text i erase?
	def removeHashtags(self):
		self.text = re.sub(r'#', '', self.text)

	def removeURLs(self):
		pass

	def removeStopWords(self):
		patternStopWords = '|'.join(self.stopWords.retrieveSet())
		self.text = re.sub(r'\b(' + patternStopWords + r')\b', '', self.text)


	def toLowerCase(self):
		self.text.lower()
