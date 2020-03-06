# Headers for reading csv files
import os
import csv

# Header for statistics
import statistics
# Header for pandas
import pandas as pd

#  Read the file
bank_csv = r"C:\Users\Ernesto\Desktop\elearning\BootCamp\TDM-REV-DATA-PT-01-2020-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"


    
# Counter for the amount of months
count = 0
total = 0
average = []
max_month = 0
min_month = 0

with open(bank_csv) as csvfile:
    budgetcsv = csv.reader(csvfile,delimiter = ',')
    next(budgetcsv, None)
    
    for row in budgetcsv:
        count = count + 1
        totals = row[1]
        total = total + int(totals)
        average.append(int(row[1]))
        
        for value in budgetcsv:
            if max(average) == value:
                max_month = value[0]
            elif min(average) == value:
                min_month = value(0)


print(count)
print(total)
print(round(statistics.mean(average)))
print(max(average))
print(min(average))
print(max_month)
print(min_month)