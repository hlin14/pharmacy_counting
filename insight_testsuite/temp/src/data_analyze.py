from collections import defaultdict

class PharmacyCounter(object):
	'''
	Do the analysis for the preprocessed data, and save to output file

	For each drug_name:
		1.count how many unique individuals who prescribed the medication
		2.calculate total drug cost

	For all drug_name:
		1.sort in descending order based on the total drug cost and if there is a tie, drug name in ascending order

	@input: preprocessed dictionary from Preprocessor
	@output: output.txt. Format: drug_name, num_prescriber, total_cost

	Usage:
		from data_analyze import PharmacyCounter
		pharmacy_counting = PharmacyCounter()
		pharmacy_counting.analyze(preprocessed_dic, output_file_name)

	made by Lin Han-Ping (hlin14@ncsu.edu)
	'''
	def __init__(self):
		self.pharmacy_counter_dic = defaultdict(list)
		self.sorted_pharmacy_counter_list = []

	def analyze(self, preprocessed_dic, output_file_name):
		'''
		Count the total number of unique individuals who prescribed the medication, and the total drug cost

		@type output_file_name: string
		@type preprocessed_dic: dictionary
		'''
		for drug_name in preprocessed_dic:
			unique_counter = set()
			drug_total_cost = 0
			for full_name, drug_cost in preprocessed_dic[drug_name]:
				if full_name not in unique_counter:
					unique_counter.add(full_name)
				drug_total_cost += drug_cost

			self.pharmacy_counter_dic[drug_name] = [len(unique_counter), round(drug_total_cost, 2)]

		'''
		Sort by the total cost
		'''
		self.sorted_pharmacy_counter_list = self.sort_by_total_cost(self.pharmacy_counter_dic)
		'''
		Save to output file
		'''
		self.output(self.sorted_pharmacy_counter_list, output_file_name)

	def sort_by_total_cost(self, pharmacy_counter_dic):
		'''
		Sort the dictionary based on 1. total_cost in descending 2.drug_name in ascending order
		@type pharmacy_counter_dic: dictionary
		@rtype sorted_pharmacy_counter_list: list
		'''
		sorted_pharmacy_counter_list = sorted(pharmacy_counter_dic.items(), key=lambda item: (-item[1][1], item[0]))
		return sorted_pharmacy_counter_list

	def output(self, sorted_pharmacy_counter_list, output_file_name):
		'''
		Save to output file
		@type sorted_pharmacy_counter_list: list
		@type output_file_name: string
		'''
		file_name = output_file_name.split("/")[-1]
		print("Now save to " + file_name + "...")
		with open(output_file_name, "w") as file:
			file.write("drug_name,num_prescriber,total_cost\n")
			for drug_item in sorted_pharmacy_counter_list:
				drug_name = drug_item[0]
				num_prescriber = drug_item[1][0]
				total_cost = drug_item[1][1]
				file.write(str(drug_name) + "," + str(num_prescriber) + "," + str(int(total_cost)) + "\n")

		file.close()