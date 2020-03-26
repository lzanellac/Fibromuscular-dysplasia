
import requests
import io
import json
import sys
import re
import time

def SubmitText(Inputfile,Bioconcept):
	
	json = {}
	
	#
	# load pmids
	#
	InputSTR=''
	with io.open(Inputfile,'r',encoding="utf-8") as file_input:
		for line in file_input:
			InputSTR = InputSTR + line
	
	#	
	# request
	#
	r = requests.post("https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/submit/"+ str(Bioconcept) , data = InputSTR)
	if r.status_code != 200 :
		print ("[Error]: HTTP code "+ str(r.status_code))
	else:
		SessionNumber = r.text.encode("utf-8")
		print ("Thanks for your submission. The session number is : " + str(SessionNumber) + "\n")
		 
		r = requests.get("https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/retrieve/" + str(SessionNumber))
		code=404
		while(code != 200):
			time.sleep(5)
			r = requests.get("https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/retrieve/" + str(SessionNumber))
			code = r.status_code
			response = r.text.encode("utf-8")
			print (code)

		print(response)


if __name__ == "__main__":

	arg_count=0
	for arg in sys.argv:
		arg_count+=1
	if arg_count<2:
		print("\npython SubmitText.py [InputFile] [Format] [BioConcept]\n\n")
		print("\t[Inputfile]: a file with a pmid list\n")
		print("\t[Bioconcept]: Gene, Disease, Chemical, Species, and Mutation. Default includes all.\n")
		print("\t* All input are case sensitive.\n\n")
		print("Eg., python SubmitText.py examples/ex.pmid Gene\n\n")
	else:
		Inputfile = sys.argv[1]
		Bioconcept = sys.argv[2]
		
		SubmitText(Inputfile,Bioconcept)


