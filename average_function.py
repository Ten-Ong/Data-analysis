# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:10:59 2022

@author: tenon
"""

# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))



def average(numbers):
    lenght = len(numbers)
    total = 0
    for num in numbers:
        total = total + num
    return total/lenght

print(average([1, 5, 9]))
print(average(range(11)))