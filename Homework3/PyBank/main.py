import os
import csv

print ("Financial Analysis")
print ("--------------------------")
csvpath = "budget_data.csv"
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

'Calculate Months'
num_lines = 0
with open(csvpath) as rowcount:
    next(rowcount)
    for i in rowcount:
        num_lines += 1
months = num_lines
print (F'Total Months: {months}')

'Add sum of cells in Profit/Loss'
nettotal = 0
with open(csvpath, newline="") as rowcount:
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)
    for a in rowcountreader:
        'print(a)'
        nettotal += int(a[1])

nettotal = '${:.2f}'.format(nettotal)
print (F'Net Total: {nettotal}')

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

AvChange = '${:.2f}'.format(int(changestotal)/totalchanges)
changestotal = '${:.2f}'.format(changestotal)
"print (F'Changes total: {changestotal}')"
print (F'Average Change: {AvChange}')


with open(csvpath, newline="") as rowcount:
    previousprofit = 867884
    greatestincrease= 0
    greatestdecrease= 0
    rowcountreader = csv.reader(rowcount, delimiter=",")
    next(rowcountreader)
    for c in rowcountreader: 
        if int(c[1]) > previousprofit:
            if int(c[1]) > greatestincrease:
                greatestincrease = (int(c[1]) - previousprofit)
                greatestincreasemonth= c[0]
            previousprofit = int(c[1])
        else:
            if int(c[1]) < greatestdecrease:
                greatestdecrease= (int(c[1]) - previousprofit)
                greatestdecreasemonth= c[0]
            previousprofit = int(c[1])

        

greatestincrease = '${:.2f}'.format(int(greatestincrease))
print (F'Greatest Increase: {greatestincreasemonth} ({greatestincrease})')
greatestdecrease = '${:.2f}'.format(int(greatestdecrease))
print (F'Greatest Decrease: {greatestdecreasemonth} ({greatestdecrease})')
                




'Total Months: 86'
'Total: $38382578'
'Average  Change: $-2315.12'
'Greatest Increase in Profits: Feb-2012 ($1926159)'
'Greatest Decrease in Profits: Sep-2013 ($-2196167)'



'The net total amount of "Profit/Losses" over the entire period'

    
    







    





