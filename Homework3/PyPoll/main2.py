import os
import csv

print ("Election Results")
print ("--------------------------")
csvpath = "election_data.csv"

'*The total number of votes cast'
num_lines = 0
with open(csvpath) as rowcount:
    next(rowcount)
    for i in rowcount:
        num_lines += 1
Number_of_Casted_Votes = num_lines
print (F'Number of Casted Votes: {Number_of_Casted_Votes}')

'* A complete list of candidates who received votes'

with open(csvpath, newline="") as election:
    next(election)
    listofcandidates = []
    Electiondata = csv.reader(election, delimiter=",")
    for word in Electiondata:
        if word[2] not in listofcandidates:
            listofcandidates.append(word[2])
print (listofcandidates)

'* The percentage of votes each candidate won'
'* The total number of votes each candidate won'

with open(csvpath, newline="") as election:
    next(election)
    Khanvotes = 0
    Correyvotes = 0
    Livotes = 0
    OTooleyvotes = 0
    Electiondata = csv.reader(election, delimiter=",")
    for word in Electiondata:
        if word[2] == "Khan":
            Khanvotes = (Khanvotes +1)
        elif word[2] == "Correy":
            Correyvotes = (Correyvotes +1)
        elif word[2] == "Li":
            Livotes = (Livotes +1)
        else:
            OTooleyvotes = (OTooleyvotes +1)

Khanpercent = ("{:.0%}".format(Khanvotes/Number_of_Casted_Votes))
Correypercent = ("{:.0%}".format(Correyvotes/Number_of_Casted_Votes))
Lipercent = ("{:.0%}".format(Livotes/Number_of_Casted_Votes))
OTooleypercent = ("{:.0%}".format(OTooleyvotes/Number_of_Casted_Votes))
print (F'Khan Vote %: {Khanpercent}')
print (F'Khan Total Votes: {Khanvotes}')
print (F'Correy Vote %: {Correypercent}')
print (F'Correy Total Votes: {Correyvotes}')
print (F'Li Vote %: {Lipercent}')
print (F'Li Total Votes: {Livotes}')
print (F"O'Tooley Vote %: {OTooleypercent}")
print (F"O'Tooley Total Votes: {OTooleyvotes}")

CandidateVotesList = [Khanvotes, Correyvotes, Livotes, OTooleyvotes]
if max(CandidateVotesList) == Khanvotes:
    print ('Khan is the winner.')
elif max(CandidateVotesList) == Correyvotes:
    print ('Correy is the winner.')
elif max(CandidateVotesList) == Livotes:
    print ('Li is the winner.')
else:
    print ("O'Tooley is the winner.")


'* The winner of the election based on popular vote.'

'* As an example, your analysis should look similar to the one below:'





    
    







    





