import rdflib
import IO
from TripleGenerator import TripleGenerator
from csvkit.utilities.csvsql import CSVSQL

def ReadMapping(location):
    file = open(location, 'r')

    #subject;file;subjectColName;objectColName;predicate
    lines = file.readlines()
    file.close()
    return lines


def YEP(PatientIDList, graph: rdflib.Graph, trippleGenerator: TripleGenerator):
    MappingInfo = ReadMapping()

    for patient in PatientIDList:
        #Burde det her ikk kun være de lines der starter med patient???
        for line in MappingInfo:
            line = line.split(';')

            match line[0]:
                case "Patient":
                    #Den burde vel få mere end en linje (alle lines der starter med patient), så tænker jeg endnu et for loop i Patient klassen
                    graph = trippleGenerator.Patient(line, graph)


            res = QueryCSV(line[1], line[2], line[3], patient)



def Main(ontPath):
    ont = rdflib.Namespace(ontPath)
    graph = rdflib.Graph()

    trippleGenerator = TripleGenerator(ont)

    csvPath = "Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv/person.csv"

    column = IO.GetColumnNum(csvPath, "person_id")
    Persons = IO.GetClassIds(csvPath, column)

    YEP(Persons, graph, trippleGenerator)
    



if __name__ == "__main__":
    # DET HER FUCKER JEG MED SENERE
    ontPath = "file:///D:/Programmering/Github/P5/KNOX-OMOP2KG/Ontology/TEST_ONT.ttl#"
    Main(ontPath)


#Indlæs alle relevante id'er