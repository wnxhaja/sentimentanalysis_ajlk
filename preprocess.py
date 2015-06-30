import re
from stopwords import StopWords

class Preprocess:

	def __init__(self, text):
		self.text = text
		self.stopWords = StopWords()
		#self.repeatingCharactersPattern = r'(.)\1{2,}'

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

	def truncateElongatedWords(self):
		re.sub(r'(.)\1{2,}', r'\1\1', self.text)

	def removeMentions(self):
		re.sub(r'@(\w+)', r'', self.text)

	#hashtags end sa text i erase
	def removeHashtags(self):
		re.sub(r'#', '', self.text)

	def removeURLs(self):
		pass

	def removeStopWords(self):
		for i in range(0, len(self.text))
			if self.stopWords.contains(self.text[i]):
				del self.text[i]

	def toLowerCase(self):
		self.text.lower()
