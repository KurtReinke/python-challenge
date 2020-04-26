#imports
import os
import csv

#create module
file1= os.path.join('Resources/election_data.csv')

#define variables
total_votes_cast=[]
candidates=[]
county=[]
khan=[0]
correy=[]
li=[0]
otooley=[]

#open file
with open(file1) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
#skip header
    header=next(csvreader)
    
#The total number of votes cast

    for row in csvreader:
        total_votes_cast=(sum(len(votes)))
        print(total_votes_cast)
        #votes.append(int(row[0]))
        #county.append(row[1])
        #candidates.append(row[2])
        
#totalvotesdict= dict[zip(candidates, votes)]        
#The total number of votes each candidate won  

#if for each candidate vote total
    for candidate in candidates:
        if row[2] == "Khan":
            khant= len(khan)
        elif row[2] == "Correy":
            correyt= len(correy)
        elif row[2] == "Li":
            lit= len(li)
        elif row[2] == "O'Tooley":
            tooleyt= len(otooley)
    
    
#Dictionary for candidates
#A complete list of candidates who received votes
    candidates_list={"Khan", "Correy", "Li", "O'Tooley"}
    print(f'{candidates}')

#The percentage of votes each candidate won
    khanp = (khant/total_votes_cast)
    correyp= (correyt/total_votes_cast)
    lip= (lit/total_votes_cast)
    otooleyp= (otooleyt/total_votes_cast)

#The winner of the election based on popular vote.
if khanp>(otooleyp, lip, correyp):
    winner="Khan!"
elif correyp>(otooleyp, lip, khanp):
    winner= "Correy!"
elif lip>(otooleyp, khanp, correyp):
    winner="Li!"
elif otooleyp>(khanp, lip, correyp):
    winner= "O'Tooley!"
    
output=os.path('python-challenge/PyPoll/"ElectionResults"')
with open(output) as file:

    print(f"Election Results")
    print(f"-------------------------------------------------")
    print(f"Total Votes Cast:{total_votes_cast}")
    print(f"-------------------------------------------------")
    print(f"Khan: {khanp}, {khant}")
    print(f"Correy: {correyp}, {correyt}")
    print(f"Li: {lip}, {lit}")
    print(f"O'Tooley: {otooleyp}, {otooleyt}")
    print(f"-------------------------------------------------")
    print(f"Winner: {winner}")
    print(f"--------------------------------------------------")
