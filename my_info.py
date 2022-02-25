# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:10:56 2022

@author: tenon
"""

my_info = {
        "name" : "Trang",
        "age" : 35,
        "hobbies" : ["watching movies", "watching funny movies"],
        "wake_up" : {
                "Mon-Fri" : 6,
                "weeken":8
                }
        }
        
print('My hobbies are ' + str(my_info["hobbies"]) )     
print(f'my hobbies are {my_info["hobbies"]}')   


print(len(my_info["hobbies"]))
print(f'{len(my_info["hobbies"])}')

print('Hello my name is ' + str(my_info["name"]))
print(f'Hello my name is {my_info["name"]}')

print('My wake up time for every morning are ' + str(my_info["wake_up"]) )
print('My wake up time for every morning are ' + str(my_info["wake_up"]["Mon-Fri"]) )
print(f'My wake up time for every morning are {my_info["wake_up"]["Mon-Fri"]} ')