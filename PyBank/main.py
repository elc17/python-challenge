# Headers for reading csv files
import os
import csv

# Header for statistics
import statistics

#  Read the file
bank_csv = r"C:\Users\Ernesto\Desktop\elearning\BootCamp\TDM-REV-DATA-PT-01-2020-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"


    
# Counter for the amount of months
count = 0

# Counter for the total amount of profit/losses
total = 0

# List for the average profit/losses
average = []

# Variables to calculate the greatest and lowest months
max_month = 0
min_month = 0
greatest = 0
gmonth = 0
lowest = 0
lmonth = 0

# Creates a text file and writes
f = open("results.txt","w+")

# Opens as csv file
with open(bank_csv) as csvfile:
    
    # Variable to read the csv file and separate it with ","
    budgetcsv = csv.reader(csvfile,delimiter = ',')
    
    # Skips the header
    next(budgetcsv, None)
    
    # For loop  to calculate the required outputs
    for row in budgetcsv:
        
        # Adds 1 to the counter of transactions 
        count = count + 1
        
        # Turns the current profit/loss value into integer
        totals = row[1]
        
        # Adds the current profit/loss to the total profits
        total = total + int(totals)
        
        # Adds the profit/loss to the list to calculate the average
        average.append(int(row[1]))
        
        # If to figure out the greatest and lowest month
        # If the current profit is larger than the greatest until now
        if int(row[1]) > greatest:
            
            # Changes the greatest to the current profit
            greatest = int(row[1])
            
            # Changes the greatest month to the current month
            gmonth = row[0]
            
        # If the current loss is larger than the biggest until now
        elif int(row[1]) < lowest:
            
            # Changes the lowest to the current loss
            lowest = int(row[1])
            
            # Changes the lowest month to the current month
            lmonth = row[0]
        
        
# Print results
print("Financial Analysis")
print("--------------------------------------------------")
print("Total months:", count)
print("Total amount:", total)
print("Average change:", round(statistics.mean(average)))
print("Greatest increase in profits:", gmonth, "(" + str(greatest) + ")")
print("Greatest decrease in profits:", lmonth, "(" + str(lowest) + ")")

# Writes the results into the .txt file
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

# Closes the .txt file
f.close