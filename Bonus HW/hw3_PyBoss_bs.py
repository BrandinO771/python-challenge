
'''
| PyBoss |
============================================================ 
BY : BRANDON STEINK 8-11-19
============================================================
INSTRUCTIONS :
-convert and export the data to use the following format :
-csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA

'''

'''IMPORTS / VARIABLES  
================================================================'''
import os
import csv
import re 
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',    'Alaska': 'AK',         'Arizona': 'AZ',        'Arkansas': 'AR',       'California': 'CA',
    'Colorado': 'CO',   'Connecticut': 'CT',    'Delaware': 'DE',       'Florida': 'FL',        'Georgia': 'GA',
    'Hawaii': 'HI',     'Idaho': 'ID',          'Illinois': 'IL',       'Indiana': 'IN',        'Iowa': 'IA',    'Kansas': 'KS',
    'Kentucky': 'KY',   'Louisiana': 'LA',      'Maine': 'ME',          'Maryland': 'MD',       'Massachusetts': 'MA',
    'Michigan': 'MI',   'Minnesota': 'MN',      'Mississippi': 'MS',    'Missouri': 'MO',       'Montana': 'MT',
    'Nebraska': 'NE',   'Nevada': 'NV',         'New Hampshire': 'NH',  'New Jersey': 'NJ',     'New Mexico': 'NM',
    'New York': 'NY',   'North Carolina': 'NC', 'North Dakota': 'ND',   'Ohio': 'OH',           'Oklahoma': 'OK',
    'Oregon': 'OR',     'Pennsylvania': 'PA',   'Rhode Island': 'RI',   'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN',  'Texas': 'TX',          'Utah': 'UT',           'Vermont': 'VT',        'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI',   'Wyoming': 'WY',
}

names_col = []
first_name_list = []
last_name_list = []
names_split = [] 
ssn_col = [] 
dates_raw = []
state_long = []
emp_id = []

'''IMPORT CSV / CREATE LISTS        
================================================================'''

file_to_analyze = os.path.join("", "Resources", "employee_data.csv")

with open(file_to_analyze, newline="", encoding='utf-8') as csvfile :
    temp_csv_data_table = csv.reader(csvfile, delimiter=",")
    csv_header = next(temp_csv_data_table )

    for column in  temp_csv_data_table :
        emp_id.append(column[0]) 
        names_col.append(column[1])
        dates_raw.append(column[2])
        ssn_col.append(column[3])
        state_long.append(column[4])
        #indv_words = re.split(" ", lines) # SPLIT  LIST AT EACH SPACES 
        #indv_sent = re.split("(?<=[.!?]) +", lines) # SPLIT AT EACH FOLLOWING PUNC
        #re.split(r'\W*', ITEMS_TO_SPLIT)  # SPLIT ANY COMBINED STRING LIKE CAT IS NOT C,A,T

'''REFORMAT STATES
================================================================'''
counter_two = 0 
states_abb = []
elements_e = 0 

for elements_e in state_long : 
    states_abb.append(us_state_abbrev[elements_e])
#       print(states_abb )

'''REFORMAT DATES
================================================================'''
counter_one = 0
dates_formated = []
elements_d = 0

for elements_d in dates_raw :
    dates_a = datetime.strptime(elements_d, "%Y-%m-%d")
    dates_b =  datetime.strftime(dates_a,"%m/%d/%Y")
    dates_formated.append(dates_b)
    #print(dates_b)
#   print(dates_formated)

'''SPLIT NAMES 1ST AND LAST 
================================================================'''
items = []
elements = 0 
item_number = 0 

for elements in names_col :

    if elements != "":
        
        names_split = re.split(" ", elements)       
        first_name_list.append(names_split[0])
        last_name_list.append(names_split[1])
#       print(f"the names split list is {names_split}")
#       print(f"the first name list is  {first_name_list} ")
#       print(f"the last  name list is  {last_name_list} ")

'''SOCIAL SECURITY REFORMAT 
================================================================='''
#like names above split the who ssn then 
#numbers.remove(5) # remove item
#then create new var full of items being the last 4 digits items 7-10 
#then join it with a existing var of ***-**-7526 
#print(f"the ssn list is  {ssn_col}") #print(f"the ssn item 1  {ssn_col[1]}")

elements_b = 0 
item_numberB = 0 
masked_ssn = [] 
ssn_split = [] 

for elements_b in ssn_col : 

    if elements_b != "":

        ssn_split = re.split(r'\W*',elements_b) # re.split(" ", items2)

        if len(ssn_split) >= 1 :           
            #ssn_last_four = [ssn_split[2] ]
            ssn_join =  ("".join(ssn_split[2]))
            #ssn_join =  ("".join(ssn_last_four))
            final_ssn = ("***-**-"+ ssn_join)
            masked_ssn.append(final_ssn)

        else:
            break
    
    else:
        break

        #print(ssn_join)
        #print("the element is " + elements)
        #print("the items are " + items)
        #print(ssn_split)       
        #print(final_ssn)

# print(f"the final ssn masked list is :  {masked_ssn}")
''' FINAL LISTS
==============================================================================='''

listC = [ "Employee ID" ,"First Name","Last Name", "DOB", "SSN","State"]
listD = [ first_name_list, last_name_list, dates_formated, masked_ssn, states_abb]

data_table_to_insert = zip( emp_id,  first_name_list, last_name_list, dates_formated, masked_ssn, states_abb )
    # Set temp variable 'output_file' with file name and destination address, used to construct our new csv file using native functions below 
new_output_file = os.path.join("newCVSBossfile2.csv")
    # below  'w' = write mode  ,    'x' = create if file doesn't exist and write,    'r' = read-only mode
with open(new_output_file, "w", newline="") as datafile:
    data_to_be_inserted = csv.writer(datafile)
    data_to_be_inserted.writerow(listC)
    data_to_be_inserted.writerows(data_table_to_insert)

print("your csv is now complete")














'''
========================================================================================================================================
END OF CODE : NOTES AND BONE YARD BELOW 
============================================================================================================================================================================
        ![Boss](Images/boss.jpg)
        I this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.
        Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:
        * Import the `employee_data.csv` file, which currently holds employee records like the below:

        ```csv
        Emp ID,Name,DOB,SSN,State
        214,Sarah Simpson,1985-12-04,282-01-8166,Florida
        15,Samantha Lara,1993-09-08,848-80-7526,Colorado
        411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
        ```
        * In summary, the required conversions are as follows:
        * The `Name` column should be split into separate `First Name` and `Last Name` columns.
        * The `DOB` data should be re-written into `MM/DD/YYYY` format.
        * The `SSN` data should be re-written such that the first five numbers are hidden from view.
        * The `State` data should be re-written as simple two-letter abbreviations.
        * Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
        Emp ID	Name	DOB	SSN	State
        0      1       2       3        4

        OUTPUT SHOULD LOOK LIKE  
        csv
        Emp ID,First Name,Last Name,DOB,SSN,State
        214,Sarah,Simpson,12/04/1985,***-**-8166,FL
        15,Samantha,Lara,09/08/1993,***-**-7526,CO
        411,Stacy,Charles,12/20/1957,***-**-8526,PA

        # ABBREV STATES 
        for w in indv_sent : 
            sent1_words = re.split(" ", w)
            total_sent1 = len(sent1_words)
            totalAvgLtrsList.append(total_sent1)

        print(names_col)
        print(names_col[1])
        element = names_col[1]
        testSplit = re.split(" ", element)
        firstName = testSplit[0]
        lastName = testSplit[1]
        print(f"the first name is {firstName} the last name is {lastName}")
'''