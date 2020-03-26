[Directory]
A. Introduction of folders
B. Instruction
C. FULL Usage

======================================================================================

A. [Introduction of folders & files]
	
	Examples:
		[examples]
	Resource codes:
		SubmitPMIDList.py
		SubmitText.py
	
B. [Instruction of PubTator annotation extraction]

	$ python SubmitPMIDList.py [InputFile] [Format] [BioConcept]
	
	[Inputfile]: a file with a pmid list
	[Format]: 1) pubtator (PubTator)
			  2) biocxml (BioC-XML)
			  3) biocjson (JSON-XML)
			  * Reference for detail of formats: https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/format/
	[Bioconcept]: Default (leave it blank) includes all bioconcepts. Otherwise, user can choose gene, disease, chemical, species, proteinmutation, dnamutation, snp, and cellline.
	
	* All input are case sensitive.
	
	Eg., python SubmitPMIDList.py examples/ex.pmid pubtator

C. [Instruction of online text processing] 
	
	$virtualenv -p python2.7 venv
	$source venv/bin/activate
	$pip install -r requirements.txt

	$ python SubmitText.py [Inputfile] [Bioconcept]
	
	[Inputfile]: a file with a pmid list
	[Bioconcept]: Mutation, Chemical, Disease, Gene, Species and CellLine
	
	* All input are case sensitive.
	
	Eg., python SubmitText.py examples/ex.pmid Gene
	
D. [Reference]

	Wei CH et. al., PubTator: a Web-based text mining tool for assisting Biocuration
	Wei CH et. al., Accelerating literature curation with text-mining tools: a case study of using PubTator to curate genes in PubMed abstracts
	Wei CH et. al., PubTator: A PubMed-like interactive curation system for document triage and literature curation
