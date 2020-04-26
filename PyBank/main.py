#Creat file paths across operating systems
import os
#Import Data/module for reading csv files
import csv
#Create/combine Module
file1= os.path.join('Resources/budget_data.csv')
#Values represented
month=[]
profitloss=[]
average=[]
bestprofits=["",""]
worstlosses=["",""]

#Open File in Read mode and store contents in the variables
with open(file1) as file:
    
    #csv reader specifies variable that holds content
    csvreader= csv.reader(file, delimiter=',')
    
    #read the header row first/skip it
    header= next(csvreader)

    #print(f"Header: {header}")
    #{Print Each Month
    #for row in csvreader:
    #print(row[0])
        
#Total Number of months included in dataset
#append total months/total profit to columns
    for row in csvreader:
        month.append(row[0])
        profitloss.append(row[1])
    print(len(month))
    
#net total amount of Profit/Losses over entire period
    plperiod= map(int,profitloss)
    total=(sum(plperiod))
    print(total)
    
#average of the changes in Profit/Losses for entire period, range not array
    for x in range(len(profitloss)-1):
        mc= int(profitloss[x+1])-int(profitloss[x])
#append to columns and create total
        average.append(mc)
    print(sum(average))

#greatest increase in profits(date and amount)
#max of profitloss, index and max for month
    bestprofits=[{profitloss.index(max(month))}, max(profitloss)]
    print(bestprofits)
#greatest decrease in losses(date and amount)
    worstprofits=[{profitloss.index(min(month))}, min(profitloss)]
    print(worstprofits)
#export text file

print(f'Financial Analysis')
print(f'---------------------------------------------)

print("Total Number of Months:" + str(month))
print("Total Revenue in period: $ " + str(profitloss))
      
print("Average Monthly Change in Revenue : $" + str(average))

print(f"Greatest Increase in Profits: {bestprofits}")

print(f"Greatest Decrease in Profits: {worstprofits}")
      
with open(main.py, "w") as file:
      txt_file.write(output)
    




    


