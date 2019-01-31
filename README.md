
# Pharmacy Data Analyzer

The purpose is to anaylze the raw pharmacy data from "Centers for Medicare & Medicaid Services",and it is built by python3.<br />

# Table of contents
1. [Problem](README.md#problem)
	1. [Input_format](README.md#Input_format)
	2. [Output_format](README.md#Output_format)
	3. [Challenges](README.md#Challenges)
2. [Approach](README.md#Approach)
	1. [Data_validation_clean_and_preprocess](README.md#Data_validation_clean_and_preprocess)
		1. [Data_validation](README.md#Data_validation)
		2. [Data_clean_and_preprocess](README.md#Data_clean_and_preprocess)
		3. [Save_to_dictionary_to_the_next_stage](README.md#Save_to_dictionary_to_the_next_stage)
	2. [Data_analysis](README.md#Data_analysis)
		1. [Identify_the_number_of_unique](README.md#Identify_the_number_of_unique)
		2. [Sort_in_order](README.md#Sort_in_order)
3. [Testing](README.md#Testing)
	1. [Generate_correct_data](README.md#Generate_correct_data)
	2. [Add_the_test_data](README.md#Add_the_test_data)
	3. [Run_pharmacy_counting.py](README.md#Run_pharmacy_counting.py)
	4. [Check](README.md#Check)
4. [Performance](README.md#Performance)
	1. [Time_Complexity](README.md#Time_Complexity)
	2. [Space_Complexity](README.md#Space_Complexity)
5. [Potential_Drawbacks](README.md#Potential_Drawbacks)
6. [Run_Instruction](README.md#Run_Instruction)
7. [Acknowledgement](README.md#Acknowledgement)

# Problem
The problem is to anaylze the raw pharmacy data, and sort the drug cost in in descending order. The code should be clean, modulized and well-tested. The repo structure should be formatted as required.

## Input_format
The input file is seperated by ",", along with "id", "prescriber_last_name", "prescriber_first_name", "drug_name", "drug_cost".<br />
for example:<br />
`1000000001,Smith,James,AMBIEN,100`<br />

## Output_format
The output file is seperated by ",", along with "drug_name", "num_prescriber", "total_cost"<br />
for example:<br />
`CHLORPROMAZINE,2,3000
`
## Challenges
In this coding challenge, there are several requirements:
  1. input data needs to be cleaned and preprocessed
  2. output need to sort in descending order based on the total drug cost and if there is a tie, drug name in ascending order
  3. code needs to be tested


# Approach
## Data_validation_clean_and_preprocess
### Data_validation
  1. Each row must have 5 columns
  2. All columns must not be empty, including continous spaces
  3. Drug_cost must be reasonable numeric, and can not be 0

,otherwise, discard the total row<br />

### Data_clean_and_preprocess
  1. For prescriber_name and drug_name, remove leading and ending spaces, turn to upper case
  2. For drug_cost, all characters must be numeric, and able to convert to float with two decimals
  
### Save_to_dictionary_to_the_next_stage
Save to a dictionary with key is drug_name, and value is the list of all record of prescriber with cost<br />

For example:<br />
`
[drug_name]:[[(prescriber_last_name_1, prescriber_first_name_1), drug_cost_1], [(prescriber_last_name_2, prescriber_first_name_2), drug_cost_2]...]
`
  
## Data_analysis
### Identify_the_number_of_unique 
Given the dictionary from stage 1, just use a unique_counter(set) to identify how many prescriber for this drug.<br />
Note that the definition of "unique" is (prescriber_last_name, prescriber_first_name) different from others.

### Sort_in_order
The little trick is to turn "drug_cost" into negative number, so that "drug_cost" and "drug_name" will all be sorted in the same ordering criteria.<br />
`sorted_pharmacy_counter_list = sorted(pharmacy_counter_dic.items(), key=lambda item: (-item[1][1], item[0]))`

# Testing
The tester.py can be founded in insight_testsuite/temp/src<br />
The testing process:
1. generate correct data
2. add the test data that need to test, then shuffle
3. run pharmacy_counting.py
4. check the "output dictionary" is equal to the "correct dictionary"

To run this program: `python3 tester.py`

## 1.Generate_correct_data
Randomly generate correct data format, each person will insert from 1 to 5 times, the drug_name is randomly selected from drug_A from drug_Z, and the cost is selected from 1 to 10 float number with 2 decimals. At the same time, save the correct dictionay for step 4 to validate.

## 2.Add_the_test_data
Add the invalid data that needs to be tested, see if the program can detect and discard. Test data example:
1. empty line
2. empty in the cols
3. wrong number of cols
4. invalid drug_cost format
then shuffle the data, and save to test_input.txt

## 3.Run_pharmacy_counting.py
Run the program, this will ouput the test_output.txt

## 4.Check
Read the test_output.txt file, and create the dictionary from this output, and check if it is the same as the correct dictionary from step 1. If the test pass will print`Test Pass!`
	,else will print `Test Fail!`


# Performance
## Time_Complexity
preprocess: O(n), n is how many char in the row, take O(1) to fill in the dictionary
data_analyze: O(m + mlogm), m is how many key(drug_name), read and count for the dictionary, and then sort

## Space_Complexity
The input file is read on the fly, only need space to store the dictionary, so the the space complexity is depending on how many keys(drug_name). 

# Potential_Drawbacks
1. name validation: it is hard to define what is the "right format" for the names, since there might be different rules for different language. The best way is to hava a "correct_name" list, it is more reasonable to import the "correct_name" list and use this list to check if the input is in this "correct_name" list, meaning it is a valid input.
2. drug name typo: same as name validation, it is hard to detect the typo if there is no a "correct drug name" list. Or maybe work with someone with pharmacy background knowledge will help developing a rule for potential typo.


# Run_Instruction
make sure the desired input file is in the input file directoty, and the input file name must be "itcont.txt"

`sh run.sh`

# Acknowledgement
This is the coding challenge for Insight Data Engineering.<br />
made by Lin Han-Ping(hlin14@ncsu.edu)
