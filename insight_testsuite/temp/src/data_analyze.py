from collections import defaultdict

class PharmacyCounter(object):

	def __init__(self):
		self.pharmacy_counter_dic = defaultdict(list)
		self.sorted_pharmacy_counter_list = []

	def analyze(self, preprocessed_dic):
		'''
		Count the total number of unique individuals who prescribed the medication, and the total drug cost
		'''

		for drug_name in preprocessed_dic:
			unique_counter = set()
			drug_total_cost = 0
			for full_name, drug_cost in preprocessed_dic[drug_name]:
				if full_name not in unique_counter:
					unique_counter.add(full_name)
				drug_total_cost += drug_cost

			self.pharmacy_counter_dic[drug_name] = [len(unique_counter), round(drug_total_cost, 2)]
			# print(len(id_counter))
			# print(drug_total_cost)
		#print(self.pharmacy_counter_dic.items())


		'''
		Sort by the total cost
		'''
		self.sorted_pharmacy_counter_list = self.sort_by_total_cost(self.pharmacy_counter_dic)
		#print(self.sorted_pharmacy_counter_list)



		'''
		Save to output file
		'''
		self.output(self.sorted_pharmacy_counter_list)




	def sort_by_total_cost(self, pharmacy_counter_dic):
		sorted_pharmacy_counter_list = sorted(pharmacy_counter_dic.items(), key=lambda item: (-item[1][1], item[0]))
		#print(sorted_pharmacy_counter_list)
		return sorted_pharmacy_counter_list


	def output(self, sorted_pharmacy_counter_list):
		print("Now save to top_cost_drug.txt...")
		with open("../output/top_cost_drug.txt", "w") as file:##file name??
			file.write("drug_name,num_prescriber,total_cost\n")
			for drug_item in sorted_pharmacy_counter_list:
				drug_name = drug_item[0]
				num_prescriber = drug_item[1][0]
				total_cost = drug_item[1][1]
				file.write(str(drug_name) + "," + str(num_prescriber) + "," + str(total_cost) + "\n")

		file.close()



