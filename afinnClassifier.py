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
		sentiments = []
		for item in data:
			word_senti = self.wordSentScore(item[0])
			emo_senti = self.emoticonSentScore(item[1])
			sentiments.append(self.classifyTotalScore(word_senti,emo_senti))

		sent_score = float(sum(sentiments))/float(len(sentiments))

		if sent_score >= 0:
			print "Sentiment is Positive with a score of %.5f" % sent_score
		else:
			print "Sentiment is Negative with a score of %.5f" % sent_score
		
		
	def wordSentScore(self, word_list):
		sentiments = []
		negators = {'not','no','never'}
		if not word_list:
			return None
		else:
			for tple in word_list:
				if tple[0] in negators:
					sentiments.append(self.afinnDict.get(tple[1],0)*-1)
				else:
					sentiments.append(self.afinnDict.get(tple[1],0))
		
		sentiment = float(sum(sentiments))/math.sqrt(len(word_list))
		return sentiment

	def emoticonSentScore(self, emoticon):
		Emo = Emoticons()
		if not emoticon:
			return None
		else:
			return Emo.getEmoticonSentiment(emoticon)

	def classifyTotalScore(self,word_senti,emo_senti):
		
		if word_senti > 0 and emo_senti == 'POS':
			return word_senti*2
		elif word_senti < 0 and emo_senti == 'POS':
			return -(word_senti)
		elif word_senti > 0 and emo_senti == 'NEG':
			return -(word_senti)
		elif word_senti < 0 and emo_senti == 'NEG':
			return word_senti*2
		elif not emo_senti:
			return word_senti
		elif not word_senti:
			if emo_senti == 'POS':
				return 1
			else:
				return -1