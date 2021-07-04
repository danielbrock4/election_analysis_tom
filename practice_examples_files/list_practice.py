my_list = [ ]
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

print(counties[-2])
print(len(counties))
print(counties[1:3])
counties.append("El Paso")
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(-1)
print(counties)
counties[2] = "El Paso"
print(counties)


counties.insert(1, "El Paso")
print(counties)
counties.pop(0)
print(counties)

my_tuple = ( )
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple)

print(counties_tuple[1])
print(counties_tuple[:2])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
counties_dict.items
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict["Arapahoe"])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 

if "Arapahoe" in counties:
    print("True")
else: 
    print("false")
    
my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 

if "El Paso" not in counties:
    print("True")
else: 
    print("false")

#OR - If one of the expressions is false, then the compound expression is true. If both expressions are false, then the compound expression is false.
x = 5
y = 5
if x == 4 or y == 4:
    print("true")
else:
    print("false")  

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso ARE IN the list of counties.")
else: 
    print("Arapahoe or El Paso IS NOT in the list of counties.")

#IF ELSE
#what is the score?
score = int(input("What is your test score"))
#detemine the grade
if score >= 90:
    print('your grade is an A')
elif score >= 80:
    print('your grade is a B') 
elif score >= 70: 
    print('your grade is a C')  
else:
    print('YOU FAILED!!!')     


#AND - If one of the expressions is false, then the compound expression is false.
x = 5
y = 5
if x == 5 and y == 5:
    print("true")
else:
    print("false")

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso ARE IN the list of counties.")
else: 
    print("Arapahoe or El Paso IS NOT in the list of counties.") 

#NOT - Evaluates a Boolean expression. The expression is true if the conditional is false.
x = 5
y = 4
if not(x > y):
    print("true")
else:
    print("false")   

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else: 
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#WHILE / condition-controlled loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

#FOR LOOP 
numbers = ()
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

#RANGE
numbers = ()
numbers = [0,1,2,3,4]
for num in range(4):
    print(num)

my_list = ()
counties = ["Arapahoe","Denver","Jefferson"] 
for i in range(len(counties)):
    print(counties[i])

#For Loops in Dictionaries
counties = {}
counties_dict =  {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)    

#For Loop Values in Dictionaries
counties = {}
counties_dict =  {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict.get(county))    
for county in counties_dict:
    print(counties_dict[county])        

#Get each dictionary
votingdata = {}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county in range(len(voting_data)):
      print(voting_data[county]['county'])        

votingdata = {}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county in range(len(voting_data)):
      print(voting_data[county]['county'])  

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
     print(county_dict['registered_voters'])  

for county_dict in voting_data:
    print(county_dict['county'])

# NO F STRINGS
my_votes = int(input("How many votes did you get in the election"))
total_votes =int(input('What is the total number of votes'))
percentage_votes = (my_votes / total_votes) * 100
print("I recieved" + str(percentage_votes) + "% of the total votes")    

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
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total number of votes.\n")
    
print(message_to_candidate)    

