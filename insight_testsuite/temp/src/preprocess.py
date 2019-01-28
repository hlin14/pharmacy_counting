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

			#TODO
			#have to check if the data is valid
			user_id = line[0]
			#prescriber_last_name = line[1]
			#prescriber_first_name = line[2]
			drug_name = line[3]
			drug_cost = float(line[4])

			self.preprocessed_dic[drug_name].append([user_id, drug_cost])

		#print(self.preprocessed_dic)
		return self.preprocessed_dic