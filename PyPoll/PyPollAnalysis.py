# This will allow us to creat file paths across
import os
# Module for reading CSV files
import csv

# Set path for files open and output
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "PyPoll_Analysis.txt")

# Open the CSV
with open(csvpath) as election_data:
    csvreader = csv.reader(election_data)
    # next()	Returns the next item in an iterable
    csv_header = next(csvreader)

    # declaring Variable that need to be calculated
    Vote_count = 0
    candidate_list = {}

    for row in csvreader:
        Vote_count = Vote_count + 1
        candidate = (row[2])
        
        # Looping through worksheet to pull names of candidate
        if candidate not in candidate_list:
            # add candidates name
            candidate_list[candidate] = 1
        # Counting names to count votes for each candidate
        else:
            candidate_list[candidate] = candidate_list[candidate] + 1
# set output as a variable 
output = (
    f"Election Results\n"
    f"-----------------------------------\n"
    f"Total Votes: {Vote_count}\n"
    f"-----------------------------------\n")

# writing in text file and print output
with open(output_path, 'w') as txtfile:
    print(output)
    txtfile.write(output)

    for names, votes in candidate_list.items():
        # print names and percentage votes and total votes of Candidate
        votes_p = votes/Vote_count*100
        candidate_out = f"{names}: {votes_p:.2f}% {votes}\n"
        #print and write candidates name percentage of vote and total votes
        print(candidate_out)
        txtfile.write(candidate_out)

        # https://datagy.io/python-get-dictionary-key-with-max-value/
        winner = max(candidate_list, key=candidate_list.get)

    # resetting output 
    output = (f"----------------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------------------\n")
    print(output)
    txtfile.write(output)

#TA helped me with setting up my vscode and cleaning up my PyPoll code to run smoothly as txt file, 
# because it was running fine in termianl but not showing same in txt file.