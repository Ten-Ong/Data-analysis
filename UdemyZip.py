# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:39:14 2022

@author: tenon
"""

import os
import csv

file = os.path.join("web_starter.csv")

title = []
price=[]
subscriber=[]
review=[]
length=[]
review_percent=[]


with open(file, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscriber.append(row[5])
        review.append(row[6])
      
        
        percent = round(int(row[6]) / int(row[5]),2)
        review_percent.append(percent)
        
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))


cleaned_csv = zip(title, price, subscriber, review, review_percent, length)

output = os.path.join("web_final.csv")

with open(output, "w", newline="") as datafile:
    write = csv.writer(datafile)
    
    write.writerow(["Title", "Price", "Subscriber", "Reviews", "Review_percent", "Length"])
   
    write.writerows(cleaned_csv)