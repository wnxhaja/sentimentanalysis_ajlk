__author__ = 'kert'

class Emoticons:

	def __init__(self):
		self.EMOTICONSLIST = {
			':)', ':D', ':(', ';)', ':-)', ':P', '=)', '(:', ';-)', ':/', 'XD', '=D', ':o', '=]', 'D:', ';D', ':]',
			':-(', '=/', '=('
		}

		self.EMOTICONSESCAPEDLIST = {
		':\)', ':D', ':\(', ';\)', ':-\)', ':P', '=\)', '\(:', ';-\)', ':/', 'XD', '=D', ':o', '=\]', 'D:', ';D', ':\]',
		':-\(', '=/', '=\('
		}

		self.POSITIVEEMOTICONS = {':)', ':D',';)', ':-)', ':P', '=)', '(:', ';-)', 'XD', '=D', ':o', '=]',';D', ':]'}

		self.NEGATIVEEMOTICONS = {':(',':/',':-(', '=/', '=('}

	def getEmoticons(self):
		return self.EMOTICONSLIST

	def getEscapedEmoticons(self):
		return self.EMOTICONSESCAPEDLIST

	def getPositiveEmoticons(self):
		return []

	def getNegativeEmoticons(self):
		return []

	def getEmoticonSentiment(self,emoticon):
		if emoticon in self.POSITIVEEMOTICONS:
			return 'POS'
		elif emoticon in self.NEGATIVEEMOTICONS:
			return 'NEG'
		else:
			print None