from collections import defaultdict
import csv

class Preprocessor(object):	
	'''
	Preprocess pharmacy raw data
	@input: raw data from Centers for Medicare & Medicaid Services, format:id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost

	Usage:
		from preprocess import Preprocessor
		preprocessor = Preprocessor()
		preprocessed_dic = preprocessor.preprocess(input_file_name)

	made by Lin Han-Ping (hlin14@ncsu.edu)
	'''
	def __init__(self):
		self.preprocessed_dic = defaultdict(list)

	def preprocess(self, input_file_name):
		'''
		read, clean and check validation for input data, tranform into dictionary,

		[drug_name]:[[(prescriber_last_name_1,prescriber_first_name_1), drug_cost_1], [(prescriber_last_name_2,prescriber_first_name_2), drug_cost_2]...]

		@type input_file_name: string
		@rtype: dictionary
		'''
		file_name = input_file_name.split("/")[-1]
		print("Now preprocess " + file_name + "...")

		with open(input_file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_counter = 0
			for line in csv_reader:
				line_counter += 1
				if line_counter == 1:
					pass
				else:
					'''
					Data validation:
						1.Each row must have 5 colimns
						2.All columns must not be empty, including continous spaces
						3.Drug_cost must be reasonable numeric, can not be 0
						,otherwise, discard the row

					Data clean and preprocess:
						1.For prescriber_name and drug_name, remove leading and ending spaces, turn to upper case
						2.For drug_cost, all characters must be numeric, and able to convert to float(two decimals), otherwise discard.
					'''
					if len(line) != 5:
						print("Error! Each line should have 5 item: " + ','.join(line))
						continue

					user_id = line[0]
					prescriber_last_name = line[1]
					prescriber_first_name = line[2]
					drug_name = line[3]
					drug_cost = line[4]

					if user_id.strip() == "" or prescriber_last_name.strip() == "" or prescriber_first_name.strip() == "" or drug_name.strip() == "" or drug_cost.strip() == "":
						print("Error! There is an empty string!")
						continue

					prescriber_last_name = prescriber_last_name.strip().upper()
					prescriber_first_name = prescriber_first_name.strip().upper()

					#drup_name: 1.remove leading and ending spaces 2.turn to upper case
					drug_name = drug_name.strip().upper()

					#drup_cost: 1.all characters must be numeric, and able to convert to float, otherwise, discard this item  2. limit to two decimals
					try:
						drug_cost = round(float(drug_cost), 2)
						if drug_cost == 0:
							print("Error! The drug_name: " + str(drug_name) + " has zero drug_cost")
							continue
					except ValueError:
						print("Error! The drug_name: " + str(drug_name) + " has an invalid drug_cost format: " + str(drug_cost))
						continue

					self.preprocessed_dic[drug_name].append([(prescriber_last_name,prescriber_first_name), drug_cost])
		return self.preprocessed_dic