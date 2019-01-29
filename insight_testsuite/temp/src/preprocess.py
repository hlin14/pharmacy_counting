from collections import defaultdict

class Preprocessor(object):	
	'''
	Preprocess pharmacy raw data
	@input: raw data from Centers for Medicare & Medicaid Services
	@ouptput:??
	'''
	def __init__(self):
		self.ouptput = None
		self.preprocessed_dic = defaultdict(list)

	def preprocess(self, inputFileName):
		fileName = inputFileName.split("/")[-1]
		print("Now preprocess " + fileName + "...")


		with open(inputFileName, "r") as file:
			contents = file.readlines()
		for line in contents[1:]:
			line = line.rstrip("\n").split(",")

			#user_id = line[0]
			prescriber_last_name = line[1]
			prescriber_first_name = line[2]
			drug_name = line[3]
			drug_cost = line[4]

			#TODO
			#have to check if the data is valid

			#names: 1.remove leading and ending spaces 2.turn to upper case 3....valid name format
			prescriber_last_name = prescriber_last_name.strip().upper()
			prescriber_first_name = prescriber_first_name.strip().upper()

			#drup_name: 1.remove leading and ending spaces 2.turn to upper case
			drug_name = drug_name.strip().upper()

			#drup_cost: 1.all characters must be numeric, and able to convert to float, otherwise, discard this item  2. limit to two decimals
			try:
				drug_cost = round(float(drug_cost), 2)
			except ValueError:
				print("Error! The drug_name: " + str(drug_name) + " has an invalid drug_cost format: " + str(drug_cost))
				continue

			self.preprocessed_dic[drug_name].append([(prescriber_last_name,prescriber_first_name), drug_cost])

		#print(self.preprocessed_dic)
		return self.preprocessed_dic