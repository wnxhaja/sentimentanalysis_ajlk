
from preprocess import Preprocess

global prep

iter = 1
print("Welcome!!!\n")
while iter == 1:
	tweet = raw_input("Please enter a tweet to be analyzed: ")
	prep = Preprocess() #load Preprocess class

	prep.printTweet(tweet)
	iter = input("Please enter 0 to exit and 1 to continue: ")
	print("\n")


print("Goodbye!!")
