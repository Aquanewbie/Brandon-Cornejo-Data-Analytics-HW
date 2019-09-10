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
    prevline = 867884
    for b in rowcountreader: 
        if int(b[1]) != prevline:
            changestotal += (int(b[1]) - prevline)
            prevline = int(b[1])

print (F'Changes total: {changestotal}')
pqt = int(changestotal)/totalchanges
print (pqt)

with open(csvpath, newline="") as rowcount:
    changestotal = 0
    totalchanges = int(months-1)
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)


'Total Months: 86'
'Total: $38382578'
'Average  Change: $-2315.12'
'Greatest Increase in Profits: Feb-2012 ($1926159)'
'Greatest Decrease in Profits: Sep-2013 ($-2196167)'



'The net total amount of "Profit/Losses" over the entire period'

    
    







    





