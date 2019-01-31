import sys
from preprocess import Preprocessor
from data_analyze import PharmacyCounter

'''
This is the main program to run preprocess.py and data_analyze.py for pharmacy data analysis.

This program is for Insight Data Engineering Coding Challenge.


made by Lin Han-Ping (hlin14@ncsu.edu)

'''

def preprocess():
	'''
	call Preprocessor to clean raw data

	@rtype: dictionary
	'''
	preprocessor = Preprocessor()
	preprocessed_dic = preprocessor.preprocess(input_file_name)
	return preprocessed_dic

def data_analyze(preprocessed_dic):
	'''
	call PharmacyCounter to analyze the data, and save to output file

	@type preprocessed_dic: dictionary
	'''
	pharmacy_counting = PharmacyCounter()
	pharmacy_counting.analyze(preprocessed_dic, output_file_name)

def main():
	preprocessed_dic = preprocess()
	data_analyze(preprocessed_dic)

if __name__ == "__main__":
	input_file_name = sys.argv[1]
	output_file_name = sys.argv[2]
	main()