import rdflib
import IO
import os
from TripleGenerator import TripleGenerator
from csvkit.utilities.csvsql import CSVSQL
from argparse import ArgumentParser

def ReadMapping(location):
    file = open(location, 'r')
    lines = []
    count = 0

    while True:
        count += 1
        line = file.readline()

        if not line:
            break

        if line[0] != "#":
            lines.append(line)

    #file;subjectColumn;objectColumn;predicate
    #lines = file.readlines()
    file.close()
    print("readmapping")
    return lines
    

def InputIngest(MappingPath, tripleGenerator: TripleGenerator):
    MappingList = ReadMapping(MappingPath)
    #count = 0

    for line in MappingList:
        line = line.split(';')

        res = IO.QueryCSV(line[0], line[1], line[2])

        for i in range(1, len(res[0])):
            #count += 1
            #print(count)
            tripleGenerator.LavTriple((line[1], res[0][i]), (line[2], res[1][i]), line[3])


def Main(ontPath):
    tripleGenerator = TripleGenerator(rdflib.Namespace(ontPath), rdflib.Graph())

    csvPath = "Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv/person.csv"
    MappingPath = "Triples.txt"

    InputIngest(MappingPath, tripleGenerator)

    print("COCK")

    tripleGenerator.GetGraph().serialize(format='xml', destination="KG2.xml")
    

if __name__ == "__main__":
    parser = ArgumentParser(description="Her skriver vi en description")
    parser.add_argument('ONTOLOGY_PATH', help="The path to the ontology we are mapping to")
    args = parser.parse_args()

    # DET HER FUCKER JEG MED SENERE
    #print("file:///" + os.getcwd() + "/Ontology/TEST_ONT.ttl#")
    args.ONTOLOGY_PATH = "file:///" + str(os.path.abspath(args.ONTOLOGY_PATH)).replace('\\', '/') + "#"
    # ontPath = "file:///" + os.getcwd().replace('\\', '/') + "/Ontology/OurOnt_Linked.ttl#"

    Main(args.ONTOLOGY_PATH)


#Indlæs alle relevante id'er