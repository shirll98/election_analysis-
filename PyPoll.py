import csv, os 
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
# Need to make the 'analysis folder' 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter 
total_votes = 0 

candidate_options = [] 
candidate_votes = {} #declare an empty dictionary to associate candidate name and vote count
candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#winning candidate and winning count tracker and percentage 
#use a decision statement to compare the number of votes each candidate received --> decision statement = if statements 
winning_candidate = "" #declare a variable that holds an empty string value for the winning candidate
winning_count = 0 #declare a varibale for the winning count equal to 0 
winning_percentage = 0 #declare a variable for the winning_percentage equal to 0 


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

   
    headers = next(file_reader) #next() skips over the header line 
    # print(headers)

    #print each row in the csv file 
    for row in file_reader: 
        #print(row)
        #Adds the total vote count to determine the total number of votes cast in the election 
        total_votes += 1 #number = number + 1 --> number += 1 
        #print(total_votes)

        #print the candidate name from each row 
        #candidate info is in the third column, indicate index in row 
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) # add candidate name to the list, if it is not in already 
            #begin tracking the candidate's vote count 
            candidate_votes[candidate_name] = 0  #dictionary_name[key] format to obtain the value for the key 
                #setting each candidate's vote to 0, so it can tally up the vote for each candidate 
            #candidate_votes[candidate_name] += 1 #increment vote count, num = num + 1 OR num += 1 
                #putting this within the if statement will result in voting of 1, we want the vote count to be looped 
        candidate_votes[candidate_name] += 1 #within the for loop but outside of the if statement 
    with open(file_to_save, "w") as txt_file:   
        #print(candidate_options)
        #print(candidate_votes)
# Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
    # Save the final vote count to the text file.
        txt_file.write(election_results)


    ## Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to terminal 
   print(candidate_results)
   txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
