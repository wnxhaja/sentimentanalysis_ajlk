import math
from emoticons import Emoticons

class Afinn:

	def __init__(self):
		self.afinnDict = self.createAfinnDict()

	def show(self):
		print self.afinnDict

	def createAfinnDict(self):
		filename = 'AFINN-111.txt'
		afinn_dict = dict(map(lambda (x, y): (x, int(y)), [xy.strip().split('\t') for xy in open(filename)]))
		return afinn_dict

	def classify(self,data):
		for item in data:
			item[0] = self.wordSentScore(item[0])
			item[1] = self.emoticonSentScore(item[1])
		print data
		
	def wordSentScore(self, word_list):
		sentiments = 0

		if not word_list:
			return None
		else:
			for tple in word_list:
				sentiments = self.afinnDict.get(tple[1],0)
		
		sentiment = float(sentiments)/math.sqrt(len(word_list))
		return sentiment

	def emoticonSentScore(self, emoticon):
		Emo = Emoticons()
		if not emoticon:
			return None
		else:
			return Emo.getEmoticonSentiment(emoticon)