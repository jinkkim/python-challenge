import csv
import numpy as np

# variables that need to define
totalMonth = 0
totalProfit = 0
averageChange = 0
month = []
profit = []
profitChange = []


# Read in the CSV file
with open('budget_data.csv', 'r') as csvfile:

    # Split the data on commas
    budgetData = csv.reader(csvfile, delimiter=',')
    header = next(budgetData)

    # Loop through the data, Separate columns into month and profit
    for row in budgetData:
        month.append(row[0]) 
        profit.append(int(row[1]))

totalMonth = len(month) # number of months
totalProfit = sum(profit) # calculate total amount of profit
averageChange = (profit[totalMonth -1] - profit[0]) / (totalMonth -1) # calculate average change 

# calculate profit change using numpy array, then change the numpy array back to list
profitChange = np.subtract(np.array(profit[1:85]),np.array(profit[0:84])).tolist()

# find max/min values and their index in order to get corresponding months 
maxChange = max(profitChange)
maxMonth = month[profitChange.index(maxChange)+1]

minChange = min(profitChange)
minMonth = month[profitChange.index(minChange)+1]


# print output in terminal
print("  Financial Analysis")
print("  ----------------------------")
print("  Total Months: {}".format(totalMonth))
print("  Total: ${}".format(totalProfit))
print("  Average  Change: ${:.2f}".format(averageChange))
print("  Greatest Increase in Profits: {} (${})".format(maxMonth, maxChange))
print("  Greatest Decrease in Profits: {} (${})".format(minMonth, minChange))

# print in textfile
with open("outputPybank.txt","w") as textFile:
    print("  Financial Analysis", file=textFile)
    print("  ----------------------------", file=textFile)
    print("  Total Months: {}".format(totalMonth), file=textFile)
    print("  Total: ${}".format(totalProfit), file=textFile)
    print("  Average  Change: ${:.2f}".format(averageChange), file=textFile)
    print("  Greatest Increase in Profits: {} (${})".format(maxMonth, maxChange), file=textFile)
    print("  Greatest Decrease in Profits: {} (${})".format(minMonth, minChange), file=textFile)