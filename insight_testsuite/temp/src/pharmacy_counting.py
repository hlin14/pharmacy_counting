import sys
from preprocess import Preprocessor
from data_analyze import PharmacyCounter


def preprocess():
	inputFileName = "../input/itcont.txt"
	preprocessor = Preprocessor()
	preprocessed_dic = preprocessor.preprocess(inputFileName)
	return preprocessed_dic

def data_analyze(preprocessed_dic):
	pharmacy_counting = PharmacyCounter()
	pharmacy_counting.analyze(preprocessed_dic)


if __name__ == "__main__":


	preprocessed_dic = preprocess()
	#print(preprocessed_dic)

	data_analyze(preprocessed_dic)




