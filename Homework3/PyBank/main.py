import os
import csv
csvpath = "budget_data.csv"
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

'Calculate Months'
num_lines = 0
with open(csvpath) as rowcount:
    next(rowcount)
    for i in rowcount:
        num_lines += 1
months = (num_lines-1)
print (months)

'Add sum of cells in Profit/Loss'
nettotal = 0
with open(csvpath, newline="") as rowcount:
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)
    for a in rowcountreader:
        print(a)
        nettotal += int(a[1])
print (nettotal)
'The average of the changes in "Profit/Losses" over the entire period'
avechangemath = float(nettotal/months)
print (avechangemath)
AveChangePercentage = (100 * avechangemath)
print (f"Average Profit between Jane 2010 and Feb 2017: {AveChangePercentage}")

'The greatest increase in profits (date and amount) over the entire period'
'The greatest decrease in losses (date and amount) over the entire period'



'The net total amount of "Profit/Losses" over the entire period'

    
    







    





