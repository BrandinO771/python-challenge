

''' SUMMARY HW-3 |  PART 1  |  PYBANK  |   BRANDON STEINKE   8-12-19

    /////////////////////////////////////////////////////////////////////////////////////////////////////
    #                                   S U M M A R Y 
    /////////////////////////////////////////////////////////////////////////////////////////////////////
    
    * Your task is to create a Python script that analyzes the records to calculate each of the following:
    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The average of the changes in "Profit/Losses" over the entire period
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in losses (date and amount) over the entire period
    * As an example, your analysis should look similar to the one below:
    * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    * Your task is to create a Python script that analyzes the records to calculate each of the following:

/////////////////////////////////////////////////////////////////////////////////////////////////////

MY THOUGHT PROCESS BELOW/ ENCLOSED - SORT OF PLAYED OUT A BIT DIFFERENT IN CODE
    assign columns to lists 
    use csv reader open file 

  A.) The total number of months included in the dataset
        1.)  which column has the months data? column = 0  dates_column
        2.)  add data to list called months 
        3.)  use the sum function to sum the list 
        4.)  save in var called total_months     

  B.) The net total amount of "Profit/Losses" over the entire period
        1.)  which column has the P and L  data? column = 1  P_L_Data  
        2.)  add data to list called P_L_Data
        3.)  use the sum function to sum the list 
        4.)  save in var called total_P_L   

  C.) The average of the changes in "Profit/Losses" over the entire period
        1.)  load the list P_L_Data to my average func 
        2.)  save in var called P_L_Avg_Chg  

  D.) The greatest increase in profits (date and amount) over the entire period
        1.) which column has the date  ?  column =     date 
        2.) iterate through the list P_L_Data comparing one to then next only storing the higher in var =  highest_P_L    
        3.) if higher value found grab the month from the month colum   save var =  highest_date 

  E.) The greatest decrease in losses (date and amount) over the entire period
        1.) which column has the date  ?  column =     date 
        2.) iterate through the list P_L_Data comparing one to then next only storing the lower in var =  lowest_P_L    
        3.) if lower value found grab the month from the month colum  save var =  lowest_date

  F.) Use the export csv to create new file with this data 
  G.) should we print data as seperate commands or print new csv as table ?

/////////////////////////////////////////////////////////////////////////////////////////////////////
#                               CODE STARTS  BELOW 
/////////////////////////////////////////////////////////////////////////////////////////////////////

'''

import os
import csv

''' THIS IS MY CUSTOM AVG FUNC
===================================================================='''

def average_func(the_input_List):
    
    total = sum(the_input_List)
    number_of_elements = (len(the_input_List))
    return total / ( number_of_elements - 1)


''' VARIABLES
===================================================================='''
listA = []  # this is my list for  ' dates     ' 
listB = []  # this is my list for  ' profit losses     ' 
newNumList = []
p_L_Avg_Chg = 0.00   
p_L_Data   = 0
dates_column = 0
total_P_L = 0
i = 0 
 
''' OPEN FILE / ASSIGN CUSTOM COLUMNS-LIST OF DATA
===================================================================='''

file_to_analyze = os.path.join(".", "Resources", "budget_data.csv")
        # use native func to open the 'file_to_analyze ' as a csv file
with open(file_to_analyze, newline="", encoding='utf-8') as csvfile :
    temp_csv_data_table = csv.reader(csvfile, delimiter=",")
    csv_header = next(temp_csv_data_table )
        # build new lists from the columns you specifiy below, that exist in our original file 'file_to_analyze' 
    for column in  temp_csv_data_table : 
        listA.append(column[0]) 
        listB.append(int(column[1]))

# // SOME INITIAL ALL CALCS 
total_months = (len(listA))
total_P_L = sum(listB)


''' FIND THE AVG 
===================================================================='''

curr_val = 0 
curr_val = listB[0]
values_x = 1 
chg_in_val_list = [] 

for values_x in listB :

      chg_val1  = values_x - curr_val        # subtract current element from prior
      chg_in_val_list.append(chg_val1)       # add result to new list 
      curr_val = values_x                 # reset value 

# print(chg_in_val_list)
avg_these_nums = chg_in_val_list
p_L_Avg_Chg = average_func(avg_these_nums)
pl_avg_formt = '${:.2f}'.format(p_L_Avg_Chg) # // for standard dollar format use :  '${:0,.2f}'.format()


''' FIND HIGHEST VAL 
===================================================================='''
# /// set a value for valuesA grabbing the first value in our list 

valuesA = chg_in_val_list[1] 
elementNum = -1 

for valuesB in chg_in_val_list:      
    elementNum +=1 
  
    if valuesA < valuesB :
        valuesA = valuesB
        highest_P_L_Date = listA[elementNum] #index of highest value to grab date from adjacent column or list item    


''' FIND LOWEST VAL 
===================================================================='''
# /// set a value for valuesA grabbing the first value in our list 
elementNumA = -1 
valuesC = chg_in_val_list[1] 

for valuesD in chg_in_val_list :

    elementNumA +=1

    if valuesC > valuesD :
        valuesC = valuesD
        lowest_P_L_Date = listA[elementNumA] # use index of highest value to grab date from adjacent column or list item    


''' MORE CALCS AND FORMATING 
===================================================================='''        
highest_P_L = valuesA
lowest_P_L = valuesC
totalAsDollars = '${}'.format(total_P_L)
lowest_P_L_Dollars = '(${})'.format(lowest_P_L)
highest_P_L_Dollars = '(${})'.format(highest_P_L)


''' FINAL LISTS
===================================================================='''

listC = [ "Total Months:",  "Total:",         "Average Change: ",    "Greatest Increase in Profits : ",              "Greatest Decrease in Profits: "]
listD = [  total_months,   totalAsDollars ,  pl_avg_formt,          highest_P_L_Date + " " + highest_P_L_Dollars,    lowest_P_L_Date + " " + lowest_P_L_Dollars ]

printable_list1 = zip(listC, listD)
printable_list2 = set(printable_list1)

# everytime I run this prints in diff order?
''' TERMINAL OUTPUT 
===================================================================='''

header_fo_terminal = '''
Financial Analysis
---------------------------- '''
print(header_fo_terminal)
for i in printable_list2 :
   # print(i) 
    print(i[0], i[1])

data_table_to_insert = zip(listC, listD)  


''' GENERATE AND  SAVE FILE 
===================================================================='''
new_output_file = os.path.join("new_csv_pybank_1.csv")

with open(new_output_file, "w", newline="") as datafile:

    data_to_be_inserted = csv.writer(datafile)
    data_to_be_inserted.writerows(data_table_to_insert)
print()
print("your csv is now complete")



''' SAMPLE OUTPUT BELOW 
====================================================================

Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

'''

