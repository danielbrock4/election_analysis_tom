# F STRINGS
my_votes = ()
my_votes = int(input("How many votes did you get in the election"))
total_votes =int(input('What is the total number of votes'))
print(f"I recieved {my_votes / total_votes * 100} % of the total votes")

counties = {}
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


    counties = {}
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes} number of votes."
    f"The total number of votes n the election was {total_votes}."
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total number of votes")
    
print(message_to_candidate)    


