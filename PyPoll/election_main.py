#import OS
import os

# import csv to read/work with data file
import csv

#Variables used
total_votes = 0

candidate_votes = {}
candidate_winner = ""

# data path
election_data_path = os.path.join(".", "Resources", "election_data.csv")

#setup
with open(election_data_path) as election_file:
    election_reader = csv.reader(election_file, delimiter = ',')

    #Read the header row
    election_header = next(election_reader)

    #Read each row of data after the header
    for row in election_reader:
        # Increment total votes
        total_votes += 1

        #Get the candidate name from the current row
        candidate = row[2]

        #If the candidate exists in the dict., increment their vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        #Otherwise, initialize their vote count to 1
        else:
            candidate_votes[candidate] = 1

#Generate the output
analysis_output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

#Calculate % of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n"

    #Check if the current candidate is the winner
    if not candidate_winner or votes > candidate_votes[candidate_winner]:
        candidate_winner = candidate

analysis_output += f"""
-------------------------
Winner: {candidate_winner}
-------------------------
"""

#Print the analysis
print(analysis_output)

#Export to a text file
output_file = "election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

print(f"The analysis has been saved to {output_file}.")

        
                                  



        


        
        

        

        
     

