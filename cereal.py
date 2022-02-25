# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:23:27 2022

@author: tenon
"""

import os
import csv

path = os.path.join("cereal.csv")

with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #next(csvreader, None) # skip header
    
    #reade the header row first, skip this part if there ia no header
    csv_header = next(csvfile)
    
    print("Header: "  + csv_header)
    
    print(f"Header: {csv_header}")
    
    
    for row in csvreader:
        
        if float(row[7]) >= 5:
            print(row[0] + " contain grams of fiber: " + row[7])