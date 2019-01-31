import random
from collections import defaultdict
import subprocess
import csv
'''
This is the test program for pharmacy_counting.py

The process is:
	1.generate correct data
	2.add the test data that need to test
	3.run pharmacy_counting.py
	4.check the "output dictionary" is equal to the "correct dictionary"

	if the test pass will print "Test Pass!"
	else will print "Test Fail!"


made by Lin Han-Ping (hlin14@ncsu.edu)
'''

def generate_correct_data():
	correct_dic = defaultdict(list)
	data = []
	data.append(["id","prescriber_last_name","prescriber_first_name", "drug_name", "drug_cost"])

	total_count = 10
	for idx in range(total_count):

		#determine how many time to insert
		insert_total = random.randint(1,5)

		for insert_idx in range(insert_total):

			prescriber_last_name = "last_name_" + str(idx)
			prescriber_first_name = "first_name_" + str(idx)

			#determine the drug_name: from drug_A ~ drug_Z
			drug_name = "DRUG_" + chr(random.randrange(97, 97 + 26)).upper()

			#determine the drug_cost: from 1 ~ 10 with 2 decimals float number
			drug_cost = round(random.uniform(1, 10), 2)

			#put id, last_name, fist_name, drug_name, drug_cost in
			data.append([str(idx), prescriber_last_name, prescriber_first_name, drug_name, str(drug_cost)])

			if correct_dic[drug_name] == []:
				correct_dic[drug_name]=[set([prescriber_last_name + "," + prescriber_first_name]), drug_cost]
			else:
				#print(correct_dic[drug_name])
				correct_dic[drug_name][0].add(prescriber_last_name + "," + prescriber_first_name)
				correct_dic[drug_name][1] += round(drug_cost, 2)
				correct_dic[drug_name][1] = round(correct_dic[drug_name][1], 2)

	for key in correct_dic.keys():
		correct_dic[key][0] = len(correct_dic[key][0])

	return data, correct_dic

def add_test_data(data):

	#desire not to appear in the final output

	#empty line
	data.append(["   "])

	#empty in the cols
	data.append(["0", " ", "first_name_0", "drug_A", "a"])

	#wrong number of cols
	data.append(["0", "last_name_0"])
	data.append(["0", "last_name_0", "first_name_0", "drug_A", "0", "0"])

	#invalid drug_cost format
	data.append(["0", "last_name_0", "first_name_0", "drug_A", "a"])
	data.append(["0", "last_name_0", "first_name_0", "drug_A", "0"])
	data.append(["0", "last_name_0", "first_name_0", "drug_A", "5.43.23"])

	#do the shuffling
	random.shuffle(data[1:])
	#save to test_input.txt
	save(data)

def save(data):
	with open("../input/test_input.txt", "w") as file:
		for line in data:
			file.write(','.join(line) + "\n")
	file.close()

def run_program():
	res = subprocess.check_output(["python3", "pharmacy_counting.py" ,"../input/test_input.txt", "../output/test_output.txt"])

def check_ouput(correct_dic):
	#collect from output.txt to check with correct_dic
	output_dic = defaultdict(list)
	with open("../output/test_output.txt") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_counter = 0
		for line in csv_reader:
			line_counter += 1
			if line_counter == 1:
				pass
			else:		
				drug_name = line[0]
				num_prescriber = int(line[1])
				total_cost = round(float(line[2]), 2)
				output_dic[drug_name] = [num_prescriber, total_cost]

	if output_dic == correct_dic:
		print("Test Pass!")
	else:
		print("Test Fail!")

def main():
	data, correct_dic = generate_correct_data()
	add_test_data(data)
	run_program()
	check_ouput(correct_dic)

if __name__ == "__main__":
	main()