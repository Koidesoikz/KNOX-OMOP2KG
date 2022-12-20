# KNOX-OMOP2KG
Converts data from the OMOP CDM, to a KG based on a general purpose ontology. Made for the AAU KNOX Superproject.

## Dependencies
- rdflib
    - To install use: `pip install rdflib`

## Relevant files:
* "Main.py"
* "IO.py"
* "TripleGenerator.py"
* All CSV files used to test are included in the repo under "Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv". These files are the MIMIC-IV demo converted to OMOP form.
* The relevant ontology files are in the Ontology folder. "Ont.ttl" is the full ontology we created, and "Ont_Linked.tll" is a linked version, containing references  to class definitions
* "Triples.txt" contains information regarding what data is loaded into the program
* "Mapping.txt" contains information regarding names of csv column and which ontology class that corresponds to

## Running the program
`python Main.py ONTOLOGY_LOCATION`
`python Main.py .\Ontology\Ont_Linked.ttl`