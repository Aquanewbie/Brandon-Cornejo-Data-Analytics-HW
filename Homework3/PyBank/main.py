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
months = num_lines
print (months)

'Add sum of cells in Profit/Loss'
nettotal = 0
with open(csvpath, newline="") as rowcount:
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)
    for a in rowcountreader:
        'print(a)'
        nettotal += int(a[1])
print (nettotal)

'The average of the changes in "Profit/Losses" over the entire period'

with open(csvpath, newline="") as rowcount:
    changestotal = 0
    totalchanges = int(months-1)
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)
    prev_line = 0
    for b in rowcountreader: 
        if b != prev_line:
            changestotal = changestotal + (int(prev_line)[1]-int(b)[1])
            prev_line = prev_line + 1
pqt = int(changestotal)/totalchanges
print (pqt)




'The net total amount of "Profit/Losses" over the entire period'

    
    







    





