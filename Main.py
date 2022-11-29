import rdflib
import IO
from TripleGenerator import TripleGenerator
from csvkit.utilities.csvsql import CSVSQL

def ReadMapping(location):
    file = open(location, 'r')

    #file;subjectColumn;objectColumn;predicate
    lines = file.readlines()
    file.close()
    print("readmapping")
    return lines
    

def YEP(MappingPath, graph: rdflib.Graph, trippleGenerator: TripleGenerator):
    MappingList = ReadMapping(MappingPath)

    for line in MappingList:
        print("Line break")
        line = line.split(';')

        res = IO.QueryCSV(line[0], line[1], line[2])

        for i in range(1, len(res[0])):
            TripleGenerator.LavTriple(res[0][i], res[1][i], line[3])

        # for data in res:
        #     TripleGenerator.LavTriple(data[0], data[1], line[3])

    # for patient in PatientIDList:
    #     #Burde det her ikk kun være de lines der starter med patient???
    #     for line in MappingList:
    #         line = line.split(';')

    #         match line[0]:
    #             case "Patient":
    #                 #Den burde vel få mere end en linje (alle lines der starter med patient), så tænker jeg endnu et for loop i Patient klassen
    #                 graph = trippleGenerator.Patient(line, graph)


    #         res = QueryCSV(line[1], line[2], line[3], patient)



def Main(ontPath):
    ont = rdflib.Namespace(ontPath)
    graph = rdflib.Graph()

    trippleGenerator = TripleGenerator(ont, graph)

    csvPath = "Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv/person.csv"
    MappingPath = "mapping.txt"

    YEP(MappingPath, graph, trippleGenerator)
    

if __name__ == "__main__":
    # DET HER FUCKER JEG MED SENERE
    ontPath = "file:///D:/Programmering/Github/P5/KNOX-OMOP2KG/Ontology/TEST_ONT.ttl#"
    Main(ontPath)


#Indlæs alle relevante id'er