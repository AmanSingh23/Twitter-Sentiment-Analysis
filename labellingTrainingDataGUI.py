# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:45:51 2018

@author: Priyanshu
"""
#importing required packages for GUI and csv file handling
from tkinter import Tk,Label,Button
import csv

#opening cleaned and preprocessed tweets file
tweetsExtracted=open("input.txt", "r")
list1=[]

#functions to be called for button action listener
def writetofile_h():
        inp="hap"
        writetofile(inp)
def writetofile_s():
        inp="sad"
        writetofile(inp)
def writetofile_a():
        inp="ang"
        writetofile(inp)
def writetofile_n():
        inp="neu"
        writetofile(inp)
def writetofile_r():
        root.destroy()
    
def writetofile(inp):
    list2=[]
    list2.append(row[:-1])
    list2.append(inp)
    list1.append(tuple(list2))
    root.destroy()

#creating GUI and displaying tweets to be labelled 
for row in tweetsExtracted:
    root = Tk()
    Label(root, text=row).pack()
    happy=Button(root,text="happy",command=writetofile_h).pack()
    sad=Button(root,text="sad",command=writetofile_s).pack()
    angry=Button(root,text="angry",command=writetofile_a).pack()
    neutral=Button(root,text="neutral",command=writetofile_n).pack()
    reject=Button(root,text="reject",command=writetofile_r).pack()
    root.mainloop()

#writing the labelled data to csv file
labelledData=open('output.csv','a')
with labelledData:
    csv_wr=csv.writer(labelledData)
    csv_wr.writerows(list1)
tweetsExtracted.close()
labelledData.close()