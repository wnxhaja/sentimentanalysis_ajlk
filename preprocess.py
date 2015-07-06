import re
from stopwords import StopWords
from emoticons import Emoticons

class Preprocess:

	def __init__(self, text):
		self.text = text
		self.stopWords = StopWords()
		self.emoticons = Emoticons()
		if not self.checkForEndingPunctuation():
			self.text = self.text + '.'
		#if not self.checkForEndingEmoticons():
		#	self.text = self.text + '.'

	#returns a list
	def preprocess(self):
		self.truncateElongatedWords()
		self.truncateElongatedPunctuations()
		self.removeMentions()
		self.removeHashtags()
		self.removeStopWords()
		self.completeContractions()
		self.removeURLs()
		return self.segmentText()

	def segmentText(self):
		segmentedText = self.splitText()
		segmentedText.pop() #pop the last element of the list. From the regex, always appends a '' on the end of the
		#  list
		segmentedText = self.tagEmoticons(segmentedText)
		segmentedText = self.truncateSuccessiveSpaces(segmentedText) #2 or more spaces is trasformed into 1 space
		segmentedText = self.toLowerCase(segmentedText)
		segmentedText = self.checkForLastSegmentElement(segmentedText) #for instances when last element of the
		# segmented text is a ''
		return segmentedText

	def splitText(self):
		pattern = '|'.join(self.emoticons.getEscapedEmoticons())
		segmentedText = re.split(r"[.?!]|(" + pattern + ")", self.text)
		return segmentedText

	def tagEmoticons(self, segmentedText):
		segmentedTextWithTaggedEmoticons = []
		iter = 0
		for i in range(len(segmentedText)):
			if i%2 == 0:    #if even
				tmpLst = [segmentedText[i]]
			else:           #if odd
				tmpLst.append(segmentedText[i])
				segmentedTextWithTaggedEmoticons.append(tmpLst)

		return segmentedTextWithTaggedEmoticons

	def truncateSuccessiveSpaces(self, segmentedText):
		newSegmentedText = []
		for segment in segmentedText:
			text = segment[0]
			text = re.sub(' +', ' ', text)
			segment = [text, segment[1]]
			newSegmentedText.append(segment)

		return newSegmentedText

	def toLowerCase(self, segmentedText):
		lowerCasedSegment = []
		for segment in segmentedText:
			text  = segment[0]
			lowerCasedSegment.append([text.lower(), segment[1]])

		return lowerCasedSegment

	def checkForEndingPunctuation(self):
		return self.text.endswith('.') or self.text.endswith('!') or self.text.endswith('?')

	def checkForLastSegmentElement(self, segmentedText):
		if segmentedText[len(segmentedText) - 1][0] == '':
			segmentedText.pop()
		return segmentedText

	def truncateElongatedWords(self):
		self.text = re.sub(r'(.)\1{2,}', r'\1\1', self.text)

	def truncateElongatedPunctuations(self):
		self.text = re.sub(r'([!?.])\1{2,}', r'\1', self.text)

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
		self.text = re.sub(r"(.+)n't", 'not', self.text)


