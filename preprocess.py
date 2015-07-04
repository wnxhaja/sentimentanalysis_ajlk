import re
from stopwords import StopWords
from emoticons import Emoticons

class Preprocess:

	def __init__(self, text):
		self.text = text
		self.stopWords = StopWords()
		self.emoticons = Emoticons()
		#self.repeatingCharactersPattern = r'(.)\1{2,}'

	#returns a list
	def preprocess(self):
		return []

	def segmentText(self):
		pattern = '|'.join(map(re.escape, self.emoticons.getEmoticons()))
		segmentedText = re.split(r"[.?!]|(" + pattern + ")", self.text)
		segmentedText = tagEmoticons(segmentedText)
		return segmentedText

	def tagEmoticons(self, segmentedText):
		return []

	def truncateElongatedWords(self):
		self.text = re.sub(r'(.)\1{2,}', r'\1\1', self.text)

	def removeMentions(self):
		self.text = re.sub(r'@(\w+)', r'', self.text)

	def removeHashtags(self):
		#remove end of text hashtag
		splitText = self.text.split(' ')
		while True:
				if splitText[len(splitText) - 1][0] == "#":
						splitText.pop()
				else:
						break
		self.text = ' '.join(splitText)

		#remove hash symbol if hashtag is not in the end of text
		self.text = re.sub(r'#', '', self.text)

	def removeURLs(self):
		self.text = re.sub(r'(\w+:\/\/\S+)*', '', self.text)

	def removeStopWords(self):
		patternStopWords = '|'.join(self.stopWords.getStopWords())
		self.text = re.sub(r'\b(' + patternStopWords + r')\b', '', self.text)

	def completeContractions(self):
		self.text = re.sub(r"([a-z]+)n't", 'not', text)

	def toLowerCase(self):
		self.text.lower()
