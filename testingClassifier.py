# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:25:03 2018

@author: Rahul Vedanta
"""

#First we’ll read some test data.
with open('test.txt') as f:
    testData = f.read().splitlines()
f.close()

#reading classifer saved in a file
import pickle
classifierFile = open('my_classifier.pickle', 'rb')
classifier = pickle.load(classifierFile)
classifierFile.close()

#variable declarations
happyTweets=0
sadTweets=0
angryTweets=0
neutralTweets=0
totalTweets=len(testData)
for tweet in testData:
    #Call the classify(text) method to use the classifier.
    sentiment=classifier.classify(tweet)
    if(sentiment=='hap'):
        happyTweets=happyTweets+1
    elif(sentiment=='sad'):
        sadTweets=sadTweets+1
    elif(sentiment=='ang'):
        angryTweets=angryTweets+1
    elif(sentiment=='neu'):
        neutralTweets=neutralTweets+1
    #print(tweet,sentiment,sep='\t')

#printing the percentage
print('Happy Tweets %: {}%'.format(happyTweets/totalTweets*100))
print('Sad Tweets %: {}%'.format(sadTweets/totalTweets*100))
print('Angry Tweets %: {}%'.format(angryTweets/totalTweets*100))
print('Neutral Tweets %: {}%'.format(neutralTweets/totalTweets*100))