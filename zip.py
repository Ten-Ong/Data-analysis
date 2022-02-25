# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:42:50 2022

@author: tenon
"""
import csv
import os


indexes = [1,2,3,4]
employees = ["Dartanion","Bernard","Jisan","Rodolfo"]
departments = ["Product","sales","Technology","Marketing"]

roster = zip(indexes, employees, departments)

path = os.path.join("zip.csv")
    
with open (path, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    
    csvwriter.writerow(["Index","Employees", "Department"])
    
    csvwriter.writerows(roster)
    
