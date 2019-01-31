
# Pharmacy Data Analyzer

The purpose is to anaylze the raw pharmacy data from "Centers for Medicare & Medicaid Services",and it is built by python3.<br />

# Table of contents

# Problem
The problem is to anaylze the raw pharmacy data, and sort the drug cost in in descending order. The code should be clean, modulized and well-tested. The repo structure should be formatted as required.

## Input format
The input file is seperated by ",", along with "id", "prescriber_last_name", "prescriber_first_name", "drug_name", "drug_cost".<br />
for example:<br />
`1000000001,Smith,James,AMBIEN,100`<br />

## Output format
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
## Stage 1: Data validation, clean and preprocess
### Data validation
  1. Each row must have 5 columns
  2. All columns must not be empty, including continous spaces
  3. Drug_cost must be reasonable numeric, and can not be 0

,otherwise, discard the total row<br />

### Data clean and preprocess
  1. For prescriber_name and drug_name, remove leading and ending spaces, turn to upper case
  2. For drug_cost, all characters must be numeric, and able to convert to float with two decimals
  
### Save to dictionary to the next stage
Save to a dictionary with key is drug_name, and value is the list of all record of prescriber with cost<br />

For example:<br />
`
[drug_name]:[[(prescriber_last_name_1, prescriber_first_name_1), drug_cost_1], [(prescriber_last_name_2, prescriber_first_name_2), drug_cost_2]...]
`
  
## stage 2: data analysis
### identify the number of unique 
Given the dictionary from stage 1, just use a unique_counter(set) to identify how many prescriber for this drug.<br />
Note that the definition of "unique" is (prescriber_last_name, prescriber_first_name) different from others.

### sort in descending order based on the total drug cost, if there is a tie, drug name in ascending order
The little trick is to turn "drug_cost" into negative number, so that "drug_cost" and "drug_name" will all be sorted in the same ordering criteria.<br />
`sorted_pharmacy_counter_list = sorted(pharmacy_counter_dic.items(), key=lambda item: (-item[1][1], item[0]))`

# Testing
The tester.py can be founded in insight_testsuite/temp/src<br />
The testing process:
1. generate correct data
2. add the test data that need to test, then shuffle
3. run pharmacy_counting.py
4. check the "output dictionary" is equal to the "correct dictionary"

## 1.generate correct data
Randomly generate correct data format, each person will insert from 1 to 5 times, the drug_name is randomly selected from drug_A from drug_Z, and the cost is selected from 1 to 10 float number with 2 decimals. At the same time, save the correct dictionay for step 4 to validate.

## 2.add the test data that need to test, and shuffle
Add the invalid data that needs to be tested, see if the program can detect and discard. Test data example:
1. empty line
2. empty in the cols
3. wrong number of cols
4. invalid drug_cost format
then shuffle the data, and save to test_input.txt

## 3.run pharmacy_counting.py
Run the program, this will ouput the test_output.txt

## 4.check the "output dictionary" is equal to the "correct dictionary"
Read the test_output.txt file, and create the dictionary from this output, and check if it is the same as the correct dictionary from step 1. If the test pass will print`Test Pass!`
	,else will print `Test Fail!`


# Performance
## Time Complexity
preprocess: O(n), n is how many char in the row, take O(1) to fill in the dictionary
data_analyze: O(m + mlogm), m is how many key(drug_name), read and count for the dictionary, and then sort

## Space Complexity
The input file is read on the fly, only need space to store the dictionary, so the the space complexity is depending on how many keys(drug_name). 

# Potential Drawbacks
1. name validation: it is hard to define what is the "right format" for the names, since there might be different rules for different language. The best way is to hava a "correct_name" list, it is more reasonable to import the "correct_name" list and use this list to check if the input is in this "correct_name" list, meaning it is a valid input.
2. drug name typo: same as name validation, it is hard to detect the typo if there is no a "correct drug name" list. Or maybe work with someone with pharmacy background knowledge will help developing a rule for potential typo.


# Run Instruction
make sure the desired input file is in the input file directoty, and the input file name must be "itcont.txt"

`sh run.sh`

# Acknowledgement
This is the coding challenge for Insight Data Engineering.<br />
made by Lin Han-Ping(hlin14@ncsu.edu)
