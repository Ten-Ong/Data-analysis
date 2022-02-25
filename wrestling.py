# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:50:26 2022

@author: tenon
"""

import os
import csv


    

wrestler_data = os.path.join("WWE-Data-2016.csv")

def print_percentages(wrestler_data):
    
    name = str(wrestler_data[0])
    win  = int(wrestler_data[1])
    loss = int(wrestler_data[2])
    draw = int(wrestler_data[3])
    
    total_matched = win + loss + draw
    
    win_percent = (win / total_matched) * 100
    loss_percent =(loss / total_matched) * 100
    draw_percent =(draw / total_matched) * 100
    
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"
        
    print(f"Stats for {name}")
    print("WIN PERCENT: ", str(win_percent) )
    print("LOSS PERCENT: " , loss_percent )
    print("DRAW PERCENT: ", draw_percent )
    print(name, "is a ", type_of_wrestler)
    
    
with open (wrestler_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
    
    check_name = input("what wrestler do you want to check? ")
    
    for row in csvreader:
        
        if check_name == row[0]:
            
            print_percentages(row)
                
