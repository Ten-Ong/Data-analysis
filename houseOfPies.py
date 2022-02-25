# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:32:31 2022

@author: tenon
"""
pie_purchases = []
print("Welcome to the house of Pies! Here are our pies:" )

pieList = ("(1)Pecan, (2)Apple Crisp, (3)Bean, (4)Banoffee, (5)Black Bun, (6)Blueberry, (7)buko, (8)Tamale, (9)Steak")

print(pieList )

choice = input("what would you like in you pie?")

choice_index = int(choice) - 1 

pieList[choice_index]

print("Great! We'll have that " + pieList[choice_index] + " right out for you")