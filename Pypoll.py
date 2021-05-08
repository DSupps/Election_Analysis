# The data we need to retrieve.
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Open file with Direct Path Method

# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter - must be set back to 0 every time we run the file
total_votes = 0

# Candidate Options - we want a list of the unique candiates, start with it empty
candidate_options = []

#Declare an empty dictionary so that we can keep a tally of votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # go through each row in the CSV file and increment total_votes by 1 to count every row
    for row in file_reader:
        total_votes += 1

        #as we go through rows we want to get the canidiates name at index 2 of each row
        candidate_name = row[2]

        #add candidate name to the candidate_options list only unique
        if candidate_name not in candidate_options:
            
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Increment each candidates vote count every time their name appears in a row to keep count
        candidate_votes[candidate_name] += 1

# Determine the % of votes for each candidate by looping through the counts
# Iterate through the candidate_options = [] to get the candidates name
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        
        #If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# Print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

