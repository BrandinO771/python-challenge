
'''
PyPoll

![Vote-Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
his concentration isn't what it used to be.)

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
* As an example, your analysis should look similar to the one below:

'''

import os
import csv

total_votes = 0 
cand_name_list = []
khan_List = []
khan_count = 0
khan_perc = 0   #  //Percent// variable = "{:.2%}".format(numberBeingFormatted)

correy_list = []
correy_count = 0 
correy_perc = 0 

li_list = []
li_count = 0 
li_perc = 0

otooley_list = []
otooley_count = 0
otooley_perc = 0 

count_list = []
perc_list = []

percents_List = []
t_votes_per_cand = []
winner = str("")
final_list_zipped = ()

file_to_analyze = os.path.join(".", "resources", "election_data.csv")

with open(file_to_analyze, newline="", encoding='utf-8') as csvfile :
    temp_csv_data_table = csv.reader(csvfile, delimiter=",")
    csv_header = next(temp_csv_data_table )

    # pull data and create custom lists 
    for column in  temp_csv_data_table :
        cand_name_list.append(column[2]) 

        if column[2] == "Khan" :
            khan_List.append(column[2])
        if column[2] == "Correy" :
            correy_list.append(column[2])               
        if column[2] == "Li" :
            li_list.append(column[2])
        if column[2] == "O'Tooley" :
            otooley_list.append(column[2])

# All Calcs 
total_votes = (len(cand_name_list))
testcount = total_votes + total_votes

khan_count = (len(khan_List))  
k_count_form = '({})'.format(khan_count)
khan_perc = khan_count / total_votes
k_p = "{:.3%}".format(khan_perc)

correy_count = (len(correy_list))
c_ct_form = '({})'.format(correy_count)
correy_perc = correy_count/ total_votes
c_p = "{:.3%}".format(correy_perc)
 
otooley_count = (len(otooley_list))
ot_ct_form = '({})'.format(otooley_count)
otooley_perc = otooley_count / total_votes
o_p = "{:.3%}".format(otooley_perc)

li_count = (len(li_list))
li_ct_form = '({})'.format(li_count)
li_perc = li_count/ total_votes
i_p = "{:.3%}".format(li_perc)


# Organize Final Lists  
header_list = [ "Candidate","Vote %", "(Total Votes)"]
cand_name_list = ["  Khan    ", "  Correy  ",  "  Li      ","  O'Tooley "]
count_List_calc = [ khan_count, correy_count, li_count, otooley_count]                                                           
perc_list = [k_p  , c_p  ,   i_p,   o_p ]
count_list = [k_count_form, c_ct_form, li_ct_form, ot_ct_form,  ]
final_list_zipped = zip( cand_name_list, perc_list, count_list )


# Find Winner using new list above 
winner_val = count_List_calc[3]
index_ctr = -1
index_pos = 0 
for x in count_List_calc  :
    index_ctr +=1 
    if winner_val < x :
        index_pos = index_ctr
        winner_val = x
        
winner = cand_name_list[index_pos]


# Terminal Print out 
print( "Election Results")
print("------------------------------------------")
print("Total Votes Cast : "  + str(total_votes) )
print("-------------------------------------------")
print(header_list[0],header_list[1],header_list[2] )

for i in final_list_zipped :
    print(i[0], i[1], i[2])

print("-----------------------------------------")
print("Winner of the Election is : " + winner )
print("------------------------------------------")
print()

# Final data / commands for output file
totalVotesLine = ["Total Votes Cast : ",  total_votes]
winnerLine = ["Winner of the Election is : ",  winner ]
data_table_to_insert = zip( cand_name_list, perc_list, count_List_calc )  
new_output_file = os.path.join("new_csv_pypoll_1.csv")


with open(new_output_file, "w", newline="") as datafile:

    data_to_be_inserted = csv.writer(datafile)
    data_to_be_inserted.writerow(totalVotesLine)
    data_to_be_inserted.writerow(header_list)
    data_to_be_inserted.writerows(data_table_to_insert)
    data_to_be_inserted.writerow(winnerLine)   

print("your csv is now complete")

'''
EXAMPLE OUTPUT BELOW 
text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''
