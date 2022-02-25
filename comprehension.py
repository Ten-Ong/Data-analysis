# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:42:08 2022

@author: tenon
"""

fish = "cat fish"
letterss = []

for foo in fish:
    letterss.append(foo)
    
print(letterss)

letters = [foo.upper() for foo in fish]

print(letters)