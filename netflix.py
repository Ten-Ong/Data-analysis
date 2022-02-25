import os
import csv

movie = input("What movie are you looking for?")

path = os.path.join("netflix_ratings.csv")

found = False

with open (path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        if row[0] == movie:
            print(row[0] + "is rated " + row[1] + " with a rating of " + row[5])
            
            found = True
            
            break
    if found is False:
        print("Sorry, seem like we don't have what are you looking for.")