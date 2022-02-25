# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:53:17 2022

@author: tenon
"""

names = []


for i in range(2):
    name = input("who do you want to invite?")
    names.append(name)
    

lowerCase = [name.lower() for name in names]

titleCase = [lowerCase.title() for lowerCase in names]

invitations = [f'Dear {name}, Please come to the wedding this Saturday.' for name in titleCase]

for invitation in invitations:
    print(invitation)