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
			id_counter = set()
			drug_total_cost = 0
			for user_id, drug_cost in preprocessed_dic[drug_name]:
				if user_id not in id_counter:
					id_counter.add(user_id)
				drug_total_cost += drug_cost

			self.pharmacy_counter_dic[drug_name] = [len(id_counter), drug_total_cost]
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
		print(sorted_pharmacy_counter_list)
		return sorted_pharmacy_counter_list


	def output(self, sorted_pharmacy_counter_list):
		print("Now save to top_cost_drug.txt")
		with open("../output/top_cost_drug.txt", "w") as file:##file name??
			file.write("drug_name,num_prescriber,total_cost\n")
			for drug_item in sorted_pharmacy_counter_list:
				drug_name = drug_item[0]
				num_prescriber = drug_item[1][0]
				total_cost = drug_item[1][1]
				file.write(str(drug_name) + "," + str(num_prescriber) + "," + str(total_cost) + "\n")

		file.close()



