import rdflib
import IO
import os
from TripleGenerator import TripleGenerator
from argparse import ArgumentParser

#Reads a file containing information about what data to extract from csv and how to load it into KG
def ReadTriples(location):
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

    file.close()
    return lines
    
#Contains the main loop of the script
def InputIngest(TriplePath, tripleGenerator: TripleGenerator):
    print("Reading triples")
    TripleList = ReadTriples(TriplePath)
    count = 0
    tripleCount = 0

    #Loading status header
    print(f"      Line      |               File               |         Observation")
    print(f"------------------------------------------------------------------------")
    #Loops over a list of strings containing information about triples to be loaded
    for line in TripleList:

        #Loading status vars and prints BEGIN
        count += 1
        currFile = line.split(";")[0].split("/")[-1]
        currOp = line.split(";")[-1] if line.split(";")[-2].split("_")[0] != "literal" else line.split(";")[-2]
        currOp = currOp.strip()
        print(f"{'Line ' + str(count) + ' of ' + str(len(TripleList)):<16}|    {currFile:<30}|    {currOp}")
        #Loading status vars and prints END
        
        #Gets the data from csv. Res contains a 2D array
        line = line.split(';')
        res = IO.QueryCSV(line[0], line[1], line[2])

        #Relations between a class and a literal
        if line[3].split('_')[0] == "literal":
            for i in range(1, len(res[0])):
                tripleCount += 1
                #print("Literal")
                tripleGenerator.LiteralTriple((line[1], res[0][i]), (res[1][i], line[4]), line[3])

        #Relations between a class and the ontology class
        elif line[3].split('_')[0] == "CLASS":
            for i in range(1, len(res[0])):
                tripleCount += 1
                tripleGenerator.OntologyTriple((line[1], res[0][i]), line[3].split('_')[1])

        #Relations between specific instances of classes
        else:
            for i in range(1, len(res[0])):
                tripleCount += 1
                #print("Object")
                tripleGenerator.ClassTriple((line[1], res[0][i]), (line[2], res[1][i]), line[3])
    print(f"Number of triples: {tripleCount}")


def Main(ontPath):
    tripleGenerator = TripleGenerator(rdflib.Namespace(ontPath), rdflib.Graph())

    csvPath = "Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv/person.csv"
    TriplePath = "Triples.txt"

    InputIngest(TriplePath, tripleGenerator)

    print("Serializing...")

    tripleGenerator.GetGraph().serialize(format='xml', destination="KG2.xml")

    print("Done")
    

if __name__ == "__main__":
    parser = ArgumentParser(description="Her skriver vi en description")
    parser.add_argument('ONTOLOGY_PATH', help="The path to the ontology we are mapping to")
    args = parser.parse_args()


    #print("file:///" + os.getcwd() + "/Ontology/TEST_ONT.ttl#")
    args.ONTOLOGY_PATH = "file:///" + str(os.path.abspath(args.ONTOLOGY_PATH)).replace('\\', '/') + "#"
    # ontPath = "file:///" + os.getcwd().replace('\\', '/') + "/Ontology/OurOnt_Linked.ttl#"

    Main(args.ONTOLOGY_PATH)