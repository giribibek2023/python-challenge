import os
import csv
 # Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
max_votes = 0

election_data_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_data_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    next(csv_reader)
     # Count the votes and track the candidates
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        # Add candidate to the dictionary or increment their vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    formatted_percentage = "{:.3f}".format(percentage)
    print(f"{candidate}: {formatted_percentage}% ({votes})")
    
    # Check if the current candidate has the most votes
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")