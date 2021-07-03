# the data we need to retrieve
    #Add our dependencies
import csv
import os
    #Assign a variable to load the path
file_to_load = os.path.join("Resources", "election_results.csv")
    #Assign a variable to save the path
file_to_save = os.path.join("analysis", "election_analysis.txt")
    #Initialize a total vote counter.
total_votes = 0 
    #Declare a new list
candidate_options = [] 
    #Declare an empty dictionary
candidate_votes = {}
    #Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0    
    #Open the election results and read the file
with open(file_to_load, 'r', encoding='UTF-8') as election_data:  
        # Read the file object with the reader function. 
    print(election_data)    
    file_reader = csv.reader(election_data)
        # Read header row
    headers = next(file_reader)
# 1. The total number of votes cast
    #Print each row in the CSV file.  
    for row in file_reader:
    #Add to the total vote count.    
        total_votes += 1
# 2. A complete list of candidates who recieved votes
    #Print the candidate name from each row
        candidate_name = row[2]
    #If the candidate does not matche any existing candidate....
        if candidate_name not in candidate_options:    
    #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
# 3. The percentage of voes each candidate won
    # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# 4. The total number of votes each candidate one
     #Determine the percentage of votes for each candidate by looping through the counts.
        #Iterate through the candidate list.
    for candidate_name in candidate_votes:
            #retrieve vote count of the candidate.
        votes = candidate_votes[candidate_name]            
            #Calculate number of votes
        voting_percentage = float(votes) / float(total_votes) * 100
            #Print out each candidate's name, vote count, and percentage of votes in the terminal
        print(f"{candidate_name}: {voting_percentage:.1f}% ({votes:,})\n")
# 5. The winner of the election vased on popular vote
        #determine winning vote coudt and candidate
        #1. Determine if the votes are greate than the winning count
        if (votes > winning_count) and (voting_percentage > winning_percentage):
            #2. If true then set winning_count = votes and winning_percent = vote_percentange
            winning_count = votes
            winning_percentage = voting_percentage
            #3 set the winning candidate equal to candidate name
            winning_candidate = candidate_name
winning_candiate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candiate_summary)       
#Print number of votes    
print(total_votes)
#Print the candidate name from each row     
print(candidate_options)
#Print the candidate vote dictionary
print(candidate_votes)

                
                             




