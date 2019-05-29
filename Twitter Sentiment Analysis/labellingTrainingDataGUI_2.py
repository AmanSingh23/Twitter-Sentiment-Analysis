# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:45:51 2018

@author: Priyanshu
"""
#importing required packages for GUI and csv file handling
from tkinter import Tk,Label,Button
import csv

#opening cleaned and preprocessed tweets file
tweetsExtracted=open('C:\\Users\\Ritesh\\Desktop\\txt\\tweet_extracted.txt', "r")
list1=[]

#functions to be called for button action listener
def writetofile_h():
        inp="hap"
        global hap,count
        hap=hap+1
        count=count+1
        writetofile(inp)
def writetofile_s():
        inp="sad"
        global sa,count
        sa=sa+1
        count=count+1
        writetofile(inp)
def writetofile_a():
        inp="ang"
        global ang,count
        ang=ang+1
        count=count+1
        writetofile(inp)
def writetofile_n():
        inp="neu"
        global neu,count
        neu=neu+1
        count=count+1
        writetofile(inp)
def writetofile_r():
        root.destroy()
    
def writetofile(inp):
    list2=[]
    list2.append(row[:-1])
    list2.append(inp)
    list1.append(tuple(list2))
    root.destroy()


from pathlib import Path

my_file = Path('C:\\Users\\Ritesh\\Desktop\\txt\\stats.txt')
if my_file.is_file()==False:
    stats=open('C:\\Users\\Ritesh\\Desktop\\txt\\stats.txt','w+')
    stats.write(str(0)+"\n")
    stats.write(str(0)+"\n")
    stats.write(str(0)+"\n")
    stats.write(str(0)+"\n")
    stats.write(str(0)+"\n")
    stats.close()


#reading the count of various sentiments previously
stats=open('C:\\Users\\Ritesh\\Desktop\\txt\\stats.txt','r')
count,hap,sa,ang,neu=map(int,stats.read().split("\n")[:-1])
stats.close()


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
labelledData=open('C:\\Users\\Ritesh\\Desktop\\txt\\output_2.csv','a')
with labelledData:
    csv_wr=csv.writer(labelledData)
    csv_wr.writerows(list1)
tweetsExtracted.close()
labelledData.close()


stats=open('C:\\Users\\Ritesh\\Desktop\\txt\\stats.txt','w+')
stats.write(str(count)+"\n")
stats.write(str(hap)+"\n")
stats.write(str(sa)+"\n")
stats.write(str(ang)+"\n")
stats.write(str(neu)+"\n")
stats.close()