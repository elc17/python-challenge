# Headers for reading csv files
import os
import csv

# Header for statistics
import statistics

# Header for counter:
from collections import Counter

total = 0
candidate = {}

#  Read the file
votes_csv = r"C:\Users\Ernesto\Desktop\elearning\BootCamp\TDM-REV-DATA-PT-01-2020-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

f = open("poll.txt", "w+")

with open(votes_csv) as csvfile:
    votescsv = csv.reader(csvfile,delimiter = ',')
    next(votescsv, None)
    
    # For loop to calculate the amoun of votes
    for row in votescsv:
            
        # Adds votes to get the total amount
        total += 1
        
        if row[2] not in candidate.keys():
                candidate[row[2]] = 1
        else:
                candidate[row[2]] = candidate[row[2]] + 1
                
percentage = {}
print("Election Results")
print("--------------------------------------------------")
print("Total votes:", total)
print("--------------------------------------------------")

f.write("Election Results\n")
f.write("--------------------------------------------------\n")
f.write("Total votes: %i\n"%total)
f.write("--------------------------------------------------\n")

for key in candidate:
    percentage[key] = round((candidate[key]/total)*100,2)
    
    print(str(key) + ":", str(percentage[key]) + "%", "(" + str(candidate[key]) + ")")
    f.write(str(key))
    f.write(":")
    f.write(str(percentage[key]))
    f.write("%")
    f.write("(")
    f.write(str(candidate[key]))
    f.write(")\n")

print("--------------------------------------------------")
f.write("--------------------------------------------------\n")
#winnerv = max(candidate.values())
winnerk = max(candidate, key = candidate.get)

print("Winner:", winnerk)
f.write("Winner:%s"%winnerk)