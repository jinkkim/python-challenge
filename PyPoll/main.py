import csv

# variables that need to define
candidate = ["Khan", "Correy", "Li", "O'Tooley"]
vote = [0, 0 , 0, 0]

# Read in the CSV file
with open('election_data.csv', 'r') as csvfile:

    # Split the data on commas
    voteData = csv.reader(csvfile, delimiter=',')
    header = next(voteData)

    # Loop through the data, Separate columns into month and profit
    for row in voteData:

        if row[2] == candidate[0]:
            vote[0] += 1
        elif row[2] == candidate[1]:
            vote[1] += 1
        elif row[2] == candidate[2]:
            vote[2] += 1
        elif row[2] == candidate[3]:
            vote[3] += 1
        else:
            pass

totalVote = sum(vote)

# find max values and determine the winner
winner = candidate[vote.index(max(vote))]
 
# print output in terminal
print("  Election Results")
print("  -------------------------")
print("  Total Votes: {}".format(totalVote))
print("  -------------------------")
print("  {} : {:.3f}% ({})".format(candidate[0], vote[0]/totalVote*100, vote[0]))
print("  {} : {:.3f}% ({})".format(candidate[1], vote[1]/totalVote*100, vote[1]))
print("  {} : {:.3f}% ({})".format(candidate[2], vote[2]/totalVote*100, vote[2]))
print("  {} : {:.3f}% ({})".format(candidate[3], vote[3]/totalVote*100, vote[3]))
print("  -------------------------")
print("  Winner: {}".format(winner))
print("  -------------------------")


# print in textfile
with open("election_data.txt","w") as textFile:
    print("  Election Results", file=textFile)
    print("  -------------------------", file=textFile)
    print("  Total Votes: {}".format(totalVote), file=textFile)
    print("  -------------------------", file=textFile)
    print("  {} : {:.3f}% ({})".format(candidate[0], vote[0]/totalVote*100, vote[0]), file=textFile)
    print("  {} : {:.3f}% ({})".format(candidate[1], vote[1]/totalVote*100, vote[1]), file=textFile)
    print("  {} : {:.3f}% ({})".format(candidate[2], vote[2]/totalVote*100, vote[2]), file=textFile)
    print("  {} : {:.3f}% ({})".format(candidate[3], vote[3]/totalVote*100, vote[3]), file=textFile)
    print("  -------------------------", file=textFile)
    print("  Winner: {}".format(winner), file=textFile)
    print("  -------------------------", file=textFile)