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

def MappingSplitter(MappingList):
    PatientMapList = []
    CaresiteMapList = []
    ConditionSuggestionMapList = []
    DrugExposureMapList = []
    ObservationMapList = []
    OrganizationMapList = []
    PayerPlanMapList = []
    ProcedureOccurenceMapList = []
    HealthcareProfessionalMapList = []
    VisitOccurenceMapList = []
    DeviceExposureMapList = []

    for line in MappingList:
        match line.split(';')[0]:
            case "Patient":
                PatientMapList.add(line)
            case "Caresite":
                CaresiteMapList.add(line)
            case "ConditionSuggestion":
                ConditionSuggestionMapList.add(line)
            case "DrugExposure":
                DrugExposureMapList.add(line)
            case "Observation":
                ObservationMapList.add(line)
            case "Organization":
                OrganizationMapList.add(line)
            case "PayerPlan":
                PayerPlanMapList.add(line)
            case "ProcedureOccurence":
                ProcedureOccurenceMapList.add(line)
            case "HealthcareProfessional":
                HealthcareProfessionalMapList.add(line)
            case "VisitOccurence":
                VisitOccurenceMapList.add(line)
            case "DeviceExposure":
                DeviceExposureMapList.add(line)
            case _:
                print("Incorrect input in MappingSplitter()")
    return [PatientMapList, CaresiteMapList, ConditionSuggestionMapList, DrugExposureMapList, ObservationMapList, OrganizationMapList, PayerPlanMapList, ProcedureOccurenceMapList, HealthcareProfessionalMapList, VisitOccurenceMapList, DeviceExposureMapList]
    
    

def YEP(PatientIDList, graph: rdflib.Graph, trippleGenerator: TripleGenerator):
    MappingList = ReadMapping()
    SegmentedMapping = MappingSplitter(MappingList)

    ObservationIDList = []

    for Patient in PatientIDList:
        for line in SegmentedMapping[0]:
            line = line.split(';')

            #res = QueryCSV(File, subjectColumn, objectColumn, value)
            #      QueryCSV(observation.csv, person_id, observation_id, Patient)

            #ObservationIDList.add(res.observation_id)
            #

    for Observation in ObservationIDList:
        for line in SegmentedMapping[4]:
            line = line.split(';')

            #res = QueryCSV(File, subjectColumn, objectColumn, value)
            #      QueryCSV(observation.csv, observation_id, provider_id, Observation)

            #ProviderIDList.add(res.provider_id)
            #


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