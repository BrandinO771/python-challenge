'''
PYTHON BONUS HW  | PyParagraph  | BRANDON STEINK  |  8-12-19
========================================================================'''
''' SUMMARY INSTRUCTIONS 
    ![Language](Images/language.png)

    In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

    Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:
    * Import a text file filled with a paragraph of your choosing.
    * Assess the passage for each of the following:
    * Approximate word count
    * Approximate sentence count
    * Approximate letter count (per word)
    * Average sentence length (in words)
    * As an example, this passage:

    > “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, 
    stood with his great sword point upwards, the red raiment of his office flapping 
    around him like the red wings of an archangel. And the King saw, he knew not how, 
    something new and overwhelming. The great green trees and the great red robes swung 
    together in the wind. The preposterous masquerade, born of his own mockery, towered 
    over him and embraced the world. This was the normal, this was sanity, this was nature, 
    and he himself, with his rationality, and his detachment and his black frock-coat, he was 
    the exception and the accident a blot of black upon a world of crimson and gold.”
    ...would yield these results:
    ```output
    Paragraph Analysis
    -----------------
    Approximate Word Count: 122
    Approximate Sentence Count: 5
    Average Letter Count: 4.6
    Average Sentence Length: 24.0
    ```
    * **Special Hint:** You may find this code snippet helpful when determining sentence length (look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):
    ```python
    import re
    re.split("(?<=[.!?]) +", paragraph)
    =================================================================================================
'''


import os 
import re
import csv


''' THIS IS MY CUSTOM AVG FUNC
========================================================================'''

def average_func(the_input_List):
    
    total = sum(the_input_List)
    number_of_elements = (len(the_input_List))
    return total / number_of_elements


''' IMPORT FILE 
========================================================================'''

file = "resources/paragraph_1.txt"  #file = "./resources/paragraph_1.txt"

with open(file, 'r') as text:  #Open the file in "read" mode ('r') and store the contents in the variable "text"
   
    lines = text.read()  # This stores a reference to a file stream # Store all of the text inside a variable called "lines"



''' CALCS AND SPLITS 
========================================================================'''
    
all_char_list =[lines]
indv_words = re.split(" ", lines) # SPLIT  LIST AT EACH SPACES 
indv_sent = re.split("(?<=[.!?]) +", lines) # SPLIT AT EACH FOLLOWING PUNC
word_count = len(indv_words)
sent_count = len(indv_sent)
#print("the indvid words are")
#print(indv_words)
#print(f"Total Words : {word_count}")
#print(f"Total Sentences : {sent_count} ")



''' ITERATE SENTENCE LIST BREAK N2 WORDS AND COUNT  
========================================================================'''

total_sent1 = 0 
totalAvgLtrsList = []
words = -1
for w in indv_sent : 

        sent1_words = re.split(" ", w)
        total_sent1 = len(sent1_words)
        totalAvgLtrsList.append(total_sent1)

# print(totalAvgLtrsList)
avg_sent_length = average_func(totalAvgLtrsList) #print(f"The Average Sent Length is:  {avg_sent_length}")

for elements in all_char_list : 
    char_count = len(elements)

total_avg_letters =  (char_count - word_count - sent_count) / word_count  
avg_letters_formt = "{:.2}".format(total_avg_letters) 



''' TERMINAL PRINT OUT 
========================================================================'''

print("Paragraph Analysis")
print("-----------------")
print(f"Approx Word Count: {word_count}")
print(f"Approx Sentence Count: {sent_count} ")
print(f"The Average Letter Per Word Count: {avg_letters_formt}")
print(f"The Average Sent Length is:  {avg_sent_length}")
print(f"The Total characters with spaces are {char_count}")
print("The Total characters without spaces are " +  str(char_count - word_count - 1))


''' FINAL LISTS AND CSV OUTPUT
========================================================================'''

listA = ["Approx Word Count:","Approx Sentence Count:", "The Average Letter Per Word Count:", "The Average Sent Length is:"   ]
listB = [ word_count, sent_count, avg_letters_formt, avg_sent_length]
data_table_to_insert = zip(listA, listB )  

new_output_file = os.path.join("", "new_para_eval.csv")
with open(new_output_file, "w", newline="") as csvfile:
    data_to_be_inserted = csv.writer(csvfile, delimiter=',')
    data_to_be_inserted.writerows(data_table_to_insert)
    
print("your csv is now complete")




'''
END OF ACTIVE CODE 
===================================================================================

# // write like this if want  to put in specific folder
# new_output_file = os.path.join("", "resources", "new_para_eval.csv")
# // write like this if want in curr folder as this file 

# below is an over engineered turd replaced by above
#words +=1    
#if words <= sent_count :
        if  words == 0    and     total_sent1  == 0  :
            sent1_words = re.split(" ", w)
            total_sent1 = len(sent1_words)
            #print(f"first sentence is  {w}")
            #print(f"sent 1 split into words: {sent1_words}")
            #print(f"the total words in this sent is {total_sent1}")
        if  words == 1    and     total_sent2  == 0  :
            sent2_words = re.split(" ", w)
            total_sent2 = len(sent2_words)
        if  words == 2    and     total_sent3  == 0  :
            sent3_words = re.split(" ", w)
            total_sent3 = len(sent3_words)
        if  words == 3    and     total_sent4  == 0  :
            sent4_words = re.split(" ", w)
            total_sent4 = len(sent4_words)
        if  words == 4    and     total_sent5  == 0  :
            sent5_words = re.split(" ", w)
            total_sent5 = len(sent5_words)

total_sent_words = [ total_sent1, total_sent2, total_sent3, total_sent4, total_sent5]
print(total_sent_words)
'''
