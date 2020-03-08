# Headers for reading csv files
import os
import csv

# Header for statistics
import statistics

# Header for counter:
from collections import Counter

# Variable for the total amount of votes
total = 0

# Dictionary for key candidate : value votes
candidate = {}

#  Read the file
votes_csv = r"C:\Users\Ernesto\Desktop\elearning\BootCamp\TDM-REV-DATA-PT-01-2020-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

# Create a .txt file to write on
f = open("poll.txt", "w+")

# Use as csv file
with open(votes_csv) as csvfile:
    
    # Reads the csv file and separates with ","
    votescsv = csv.reader(csvfile,delimiter = ',')
    
    # Skips the header
    next(votescsv, None)
    
    # For loop to calculate the amoun of votes
    for row in votescsv:
            
        # Adds votes to get the total amount
        total += 1
        
        # If the current candidate doesn't exist in the dictionary
        if row[2] not in candidate.keys():
            
            # Creates the key and sets value to 1
            candidate[row[2]] = 1
        else:
            
            # If the key exists in the dictionary, add 1 to the value
            candidate[row[2]] = candidate[row[2]] + 1

# Dictionary for key candidate : value percentage    
percentage = {}

# Prints the first answers
print("Election Results")
print("--------------------------------------------------")
print("Total votes:", total)
print("--------------------------------------------------")

# Writes the first answers to the .txt file
f.write("Election Results\n")
f.write("--------------------------------------------------\n")
f.write("Total votes: %i\n"%total)
f.write("--------------------------------------------------\n")

# For loop to turn the vote numbers into percentages
for key in candidate:
    
    # Rounds the percentage calculation on each candidate vote value for each key
    percentage[key] = round((candidate[key]/total)*100,2)
    
    # Prints the results
    print(str(key) + ":", str(percentage[key]) + "%", "(" + str(candidate[key]) + ")")
    
    # Writes the results into the .txt file
    f.write(str(key))
    f.write(":")
    f.write(str(percentage[key]))
    f.write("%")
    f.write("(")
    f.write(str(candidate[key]))
    f.write(")\n")

# Prints the line
print("--------------------------------------------------")
f.write("--------------------------------------------------\n")

#winnerv = max(candidate.values())

# Get the candidate with the maximum votes
winnerk = max(candidate, key = candidate.get)

# Print the answer
print("Winner:", winnerk)

# Write the answer into a .txt file
f.write("Winner:%s"%winnerk)

# Closes the .txt file
f.close