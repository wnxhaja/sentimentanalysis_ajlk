
class FeatureExtract:

	def __init__(self, text):
		self.text = text
		self.getBigrams = self.extractBigrams(2)

	def extractBigrams(self, number):
		text_list = self.text.split()

		if len(text_list) == 1:
			text_list.insert(0, None)

		bigrams = self.find_ngrams(text_list, number)
		return bigrams

	def find_ngrams(self, text_list, number):
		return zip(*[text_list[i:] for i in range(number)])	