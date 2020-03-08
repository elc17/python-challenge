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
greatest = 0
gmonth = 0
lowest = 0
lmonth = 0

f = open("results.txt","w+")

with open(bank_csv) as csvfile:
    budgetcsv = csv.reader(csvfile,delimiter = ',')
    next(budgetcsv, None)
    
    for row in budgetcsv:
        count = count + 1
        totals = row[1]
        total = total + int(totals)
        average.append(int(row[1]))
        
        if int(row[1]) > greatest:
            greatest = int(row[1])
            gmonth = row[0]
        elif int(row[1]) < lowest:
            lowest = int(row[1])
            lmonth = row[0]
        
        

print("Financial Analysis")
print("--------------------------------------------------")
print("Total months:", count)
print("Total amount:", total)
print("Average change:", round(statistics.mean(average)))
print("Greatest increase in profits:", gmonth, "(" + str(greatest) + ")")
print("Greatest decrease in profits:", lmonth, "(" + str(lowest) + ")")

f.write("Financial Analysis\n")
f.write("-------------------------------------------------\n")
f.write("Total months: %i\n"%count)
f.write("Total amount: %i\n"%total)
f.write("Average change: %i\n"%round(statistics.mean(average)))
f.write("Greatest increase in profits: %s"%gmonth)
f.write("(%i"%greatest)
f.write(")\n")
f.write("Greatest decrease in profits: %s"%lmonth)
f.write("(%i"%lowest)
f.write(")")
f.close