__author__ = 'kert'

class Emoticons:

	def __init__(self):
		self.EMOTICONSLIST = {
			':)', ':D', ':(', ';)', ':-)', ':P', '=)', '(:', ';-)', ':/', 'XD', '=D', ':o', '=]', 'D:', ';D', ':]',
			':-(', '=/', '=('
		}

	def getEmoticons(self):
		return self.EMOTICONSLIST

	def getPositiveEmoticons(self):
		return []

	def getNegativeEmoticons(self):
		return []