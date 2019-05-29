# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:24:59 2018

@author: Rahul Vedanta
"""

#First we’ll read some training data.
import csv
trainData=[]

#opening and reading the labelled data csv file
with open('C:\\Users\\Ritesh\\Desktop\\txt\\output_1.csv') as trainingFile:
    reader = csv.reader(trainingFile, delimiter=',')
    for row in reader:
        if len(row)!=0:
            trainData.append(tuple(row))
trainingFile.close()

#Now we’ll create a Naive Bayes classifier, passing the training data into the constructor.
from textblob.classifiers import NaiveBayesClassifier
classifier = NaiveBayesClassifier(trainData)

#write classifier to file
import pickle
f = open('C:\\Users\\Ritesh\\Desktop\\txt\\myClassifier_1.pickle', 'wb')
pickle.dump(classifier, f)
f.close()