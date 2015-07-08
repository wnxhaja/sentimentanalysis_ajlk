
from preprocess import Preprocess
from featureExtract import FeatureExtract
from afinnClassifier import Afinn
from emoticons import Emoticons

global prep

iter = 1
print("Welcome!!!\n")
while iter == 1:
	tweet = raw_input("Please enter a tweet to be analyzed: ")
	prep = Preprocess(tweet) #load Preprocess class

	#preprocess input data
	data = prep.preprocess()
	print data

	#generate bigrams from preprocessed text
	for item in data:
		if not item[0]:
			item[0] = None
		else:
			bigrams = FeatureExtract(item[0]).getBigrams
			item[0] = bigrams
	print data
	
	A = Afinn()
	A.classify(data)


	iter = input("Please enter 0 to exit and 1 to continue: ")
	print("\n")

print("Goodbye!!")

