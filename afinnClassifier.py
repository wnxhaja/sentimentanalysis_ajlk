import math
from emoticons import Emoticons

class Afinn:

	def __init__(self):
		self.afinnDict = self.createAfinnDict()

	def show(self):
		print self.afinnDict

	def createAfinnDict(self):
		filename = 'AFINN-111.txt'
		afinn = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in open(filename)]))
		return afinn

	def classify(self,data):
		for item in data:
			item[0] = self.wordSentScore(item[0])
			item[1] = self.emoticonSentScore(item[1])
		#print data
		
	def wordSentScore(self, word_list):
		if not word_list:
			return None
		else:
			for tple in word_list:
				pass

	def emoticonSentScore(self, emoticon):
		Emo = Emoticons()
		if not emoticon:
			return None
		else:
			return Emo.getEmoticonSentiment(emoticon)