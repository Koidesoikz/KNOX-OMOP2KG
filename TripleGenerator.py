from rdflib import Literal, URIRef, RDF
from rdflib.namespace import XSD

class TripleGenerator():
    # graph = None
    # namespace = None

    def __init__(self, namespace, graph):
        self.namespace = namespace
        self.graph = graph

    def GetGraph(self):
        return self.graph

    def SetGraph(self, graph):
        self.graph = graph

    #Creates a URI based on the ID of the instance of the class
    def GetClassURI(self, classTuple):
        classColumnName, classID = classTuple
        return URIRef(str("http://www.example.com/" + self.GetPartialURI(classColumnName) + "/" + classID))

    #Returns a reference to a predicate
    def GetPredicateURI(self, name):
        name = name.strip()

        match name:
            case "located_at":
                return self.namespace.located_at
            case "has_observation":
                return self.namespace.has_observation
            case "subject_to":
                return self.namespace.subject_to
            case "has_exposure":
                return self.namespace.has_exposure
            case "has_suggestion":
                return self.namespace.has_suggestion
            case "hospital_org":
                return self.namespace.hospital_org
            case "condsugg_healthpro":
                return self.namespace.condsugg_healthpro
            case "drugexp_drugcost":
                return self.namespace.drugexp_drugcost
            case "drugexp_healthpro":
                return self.namespace.drugexp_healthpro
            case "obs_healthpro":
                return self.namespace.obs_healthpro
            case "payerplan_drugcost":
                return self.namespace.payerplan_drugcost
            case "payerplan_procedurecost":
                return self.namespace.payerplan_procedurecost
            case "patient_obsperiod":
                return self.namespace.patient_obsperiod
            case "patient_healthpro":
                return self.namespace.patient_healthpro
            case "patient_condperiod":
                return self.namespace.patient_condperiod
            case "patient_death":
                return self.namespace.patient_death
            case "patient_cohort":
                return self.namespace.patient_cohort
            case "patient_druginfperiod":
                return self.namespace.patient_druginfperiod
            case "patient_visitocc":
                return self.namespace.patient_visitocc
            case "patient_payerplan":
                return self.namespace.patient_payerplan
            case "patient_constdose":
                return self.namespace.patient_constdose
            case "patient_obs":
                return self.namespace.patient_obs
            case "patient_labspecimen":
                return self.namespace.patient_labspecimen
            case "patient_procedureocc":
                return self.namespace.patient_procedureocc
            case "procedureocc_procedureocc":
                return self.namespace.procedureocc_procedureocc
            case "procedureocc_healthproI":
                return self.namespace.procedureocc_healthproI
            case "procedureocc_healthproII":
                return self.namespace.procedureocc_healthproII
            case "healthpro_hospital":
                return self.namespace.healthpro_hospital
            case "visitocc_obs":
                return self.namespace.visitocc_obs
            case "visitocc_note":
                return self.namespace.visitocc_note
            case "visitocc_devexp":
                return self.namespace.visitocc_devexp
            case "visitocc_healthpro":
                return self.namespace.visitocc_healthpro
            case "visitocc_measurement":
                return self.namespace.visitocc_measurement
            case "visitocc_procedureocc":
                return self.namespace.visitocc_procedureocc
            case "devexp_healthpro":
                return self.namespace.devexp_healthpro
            case "measurement_patient":
                return self.namespace.measurement_patient
            case "measurement_healthpro":
                return self.namespace.measurement_healthpro
            case "note_healthpro":
                return self.namespace.note_healthpro
            case "note_patient":
                return self.namespace.note_patient
            case "hasI":
                return self.namespace.hasI
            case "hasII":
                return self.namespace.hasII
            case "literal_measurementvalue" :
                return self.namespace.literal_measurementvalue
            case "literal_deviceexposurestartdate":
                return self.namespace.literal_deviceexposurestartdate
            case "literal_hospitalname":
                return self.namespace.literal_hospitalname
            case "literal_cohortname":
                return self.namespace.literal_cohortname
            case "literal_cohortdescription":
                return self.namespace.literal_cohortdescription
            case "literal_cohorttype":
                return self.namespace.literal_cohorttype
            case "literal_cohortinitiationdate":
                return self.namespace.literal_cohortinitiationdate
            case "literal_conditionperiodname":
                return self.namespace.literal_conditionperiodname
            case "literal_conditiontype":
                return self.namespace.literal_conitiontype
            case "literal_conditionerastart":
                return self.namespace.literal_conditionerastart
            case "literal_conditioneraend":
                return self.namespace.literal_conditioneraend
            case "literal_conditionoccurencecount":
                return self.namespace.literal_conditionoccurencecount
            case "literal_conditionname":
                return self.namespace.literal_conditionname
            case "literal_conditiontype":
                return self.namespace.literal_conditiontype
            case "literal_conditionstartdate":
                return self.namespace.literal_conditionstartdate
            case "literal_conditionenddate":
                return self.namespace.literal_conditionenddate
            case "literal_stopreason":
                return self.namespace.literal_stopreason
            case "literal_causeofdeath":
                return self.namespace.literal_causeofdeath
            case "literal_deathtype":
                return self.namespace.literal_deathtype
            case "literal_deathdate":
                return self.namespace.literal_deathdate
            case "literal_drugname":
                return self.namespace.literal_drugname
            case "literal_drugtype":
                return self.namespace.literal_drugtype
            case "literal_drugexposurecount":
                return self.namespace.literal_drugexposurecount
            case "literal_drugerastartdate":
                return self.namespace.literal_drugerastartdate
            case "literal_drugeraenddate":
                return self.namespace.literal_drugeraenddate
            case "literal_gapdays":
                return self.namespace.literal_gapdays
            case "literal_drugname":
                return self.namespace.literal_drugname
            case "literal_drugtype":
                return self.namespace.literal_drugtype
            case "literal_stopreason":
                return self.namespace.literal_stopreason
            case "literal_refills":
                return self.namespace.literal_refills
            case "literal_quantity":
                return self.namespace.literal_quantity
            case "literal_drugexposurestartdate":
                return self.namespace.literal_drugexposurestartdate
            case "literal_drugexposureenddate":
                return self.namespace.literal_drugexposureenddate
            case "literal_sig":
                return self.namespace.literal_sig
            case "literal_lotnumber":
                return self.namespace.literal_lotnumber
            case "literal_dayssupply":
                return self.namespace.literal_dayssupply
            case "literal_state":
                return self.namespace.literal_state
            case "literal_county":
                return self.namespace.literal_county
            case "literal_address1":
                return self.namespace.literal_address1
            case "literal_address2":
                return self.namespace.literal_address2
            case "literal_city":
                return self.namespace.literal_city
            case "literal_zip":
                return self.namespace.literal_zip
            case "literal_observationname":
                return self.namespace.literal_observationname
            case "literal_observationtype":
                return self.namespace.literal_observationtype
            case "literal_observationdatetime":
                return self.namespace.literal_observationdatetime
            case "literal_observationresult":
                return self.namespace.literal_observationresult
            case "literal_birthdatetime":
                return self.namespace.literal_birthdatetime
            case "literal_gender":
                return self.namespace.literal_gender
            case "literal_race":
                return self.namespace.literal_race
            case "literal_ethnicity":
                return self.namespace.literal_ethnicity
            case "literal_procedurename":
                return self.namespace.literal_procedurename
            case "literal_proceduretype":
                return self.namespace.literal_proceduretype
            case "literal_proceduremodifier":
                return self.namespace.literal_proceduremodifier
            case "literal_proceduredatetime":
                return self.namespace.literal_proceduredatetime
            case "literal_quantity":
                return self.namespace.literal_quantity
            case "literal_speciality":
                return self.namespace.literal_speciality
            case "literal_dea":
                return self.namespace.literal_dea
            case "literal_npi":
                return self.namespace.literal_npi
            case "literal_gender":
                return self.namespace.literal_gender
            case "literal_yearofbirth":
                return self.namespace.literal_yearofbirth
            case "literal_visittype":
                return self.namespace.literal_visittype
            case "literal_visitstartdate":
                return self.namespace.literal_visitstartdate
            case "literal_visitenddate":
                return self.namespace.literal_visitenddate
            case "literal_devicename":
                return self.namespace.literal_devicename
            case "literal_deviceexposurestartdate":
                return self.namespace.literal_deviceexposurestartdate
            case "literal_deviceexposureenddate":
                return self.namespace.literal_deviceexposureenddate
            case "literal_devicetype":
                return self.namespace.literal_devicetype
            case "literal_quantity":
                return self.namespace.literal_quantity
            case "literal_dosevalue":
                return self.namespace.literal_dosevalue
            case "literal_doseerastartdate":
                return self.namespace.literal_doseerastartdate
            case "literal_doseeraenddate":
                return self.namespace.literal_doseeraenddate
            case "literal_amountvalue":
                return self.namespace.literal_amountvalue
            case "literal_amountunit":
                return self.namespace.literal_amountunit
            case "literal_concentrationvalue":
                return self.namespace.literal_concentrationvalue
            case "literal_concentrationunit":
                return self.namespace.literal_concentrationunit
            case "literal_measurementdate":
                return self.namespace.literal_measurementdate
            case "literal_measurementtype":
                return self.namespace.literal_measurementtype
            case "literal_normalrangelow":
                return self.namespace.literal_normalrangelow
            case "literal_normalrangehigh":
                return self.namespace.literal_normalrangehigh
            case "literal_measurementvalue":
                return self.namespace.literal_measurementvalue
            case "literal_unitvalue":
                return self.namespace.literal_unitvalue
            case "literal_notedate":
                return self.namespace.literal_notedate
            case "literal_notetype":
                return self.namespace.literal_notetype
            case "literal_noteclass":
                return self.namespace.literal_noteclass
            case "literal_notetitle":
                return self.namespace.literal_notetitle
            case "literal_language":
                return self.namespace.literal_language
            case "literal_notevalue":
                return self.namespace.literal_notevalue
            case "literal_observationperiodstartdatetime":
                return self.namespace.literal_observationperiodstartdatetime
            case "literal_observationperiodenddatetime":
                return self.namespace.literal_observationperiodenddatetime
            case "literal_periodtype":
                return self.namespace.literal_periodtype
            case "literal_specimentype":
                return self.namespace.literal_specimentype
            case "literal_specimendatetime":
                return self.namespace.literal_specimendatetime
            case "literal_quantity":
                return self.namespace.literal_quantity
            case "literal_unit":
                return self.namespace.literal_unit
            case "literal_anatomicsite":
                return self.namespace.literal_anatomicsite
            case "literal_diseasestatus":
                return self.namespace.literal_diseasestatus
            case "literal_specimenvalue":
                return self.namespace.literal_specimenvalue
            case "literal_measurementvalue":
                return self.namespace.literal_measurementvalue
            case _:
                print("yoooo, shit broke in GetPredicateURI")
                print(name)
                return

    def ClassTriple(self, subject, object, predicate):
        self.graph.add((self.GetClassURI(subject), self.GetPredicateURI(predicate), self.GetClassURI(object)))

    def LiteralTriple(self, subject, object, predicate):
        self.graph.add((self.GetClassURI(subject), self.GetPredicateURI(predicate), self.GetLiteral(object)))

    def OntologyTriple(self, subject, object):
        self.graph.add((self.GetClassURI(subject), RDF.type, self.GetClass(object)))

    #Returns a reference to a class
    def GetClass(self, name):
        name = name.strip()
        match name:
            case "Hospital":
                return self.namespace.Hospital
            case "Cohort":
                return self.namespace.Cohort
            case "ConditionPeriod":
                return self.namespace.ConditionPeriod
            case "ConditionSuggestion":
                return self.namespace.ConditionSuggestion
            case "Death":
                return self.namespace.Death
            case "DrugCost":
                return self.namespace.DrugCost
            case "DrugInfluencePeriod":
                return self.namespace.DrugInfluencePeriod
            case "DrugExposure":
                return self.namespace.DrugExposure
            case "Location":
                return self.namespace.Location
            case "Observation":
                return self.namespace.Observation
            case "Organization":
                return self.namespace.Organization
            case "PayerPlan":
                return self.namespace.PayerPlan
            case "Patient":
                return self.namespace.Patient
            case "ProcedureCost":
                return self.namespace.ProcedureCost
            case "ProcedureOccurence":
                return self.namespace.ProcedureOccurence
            case "HealthcareProfesional":
                return self.namespace.HealthcareProfesional
            case "VisitOccurence":
                return self.namespace.VisitOccurence
            case "DeviceExposure":
                return self.namespace.DeviceExposure
            case "ConstantDosePeriod":
                return self.namespace.ConstantDosePeriod
            case "DrugStrength":
                return self.namespace.DrugStrength
            case "Measurement":
                return self.namespace.Measurement
            case "Note":
                return self.namespace.Note
            case "ObservationPeriod":
                return self.namespace.ObservationPeriod
            case "LaboratorySpecimen":
                return self.namespace.LaboratorySpecimen
            case _:
                print("get class shit broke")
                return
        
    #returns a reference to a literal
    def GetLiteral(self, data):
        value, type = data
        type = type.strip()

        match type:
            case "integer":
                if value == "":
                    return Literal(None, datatype=XSD.integer)
                else:
                    return Literal(int(value), datatype=XSD.integer)
            case "float":
                if value == "":
                    return Literal(None, datatype=XSD.float)
                else:
                    return Literal(float(value), datatype=XSD.float)
            case "dateTime":
                if value == "":
                    return Literal(None, datatype=XSD.integer)
                else:
                    #HER ER DER MÅSKE EN FEJL! Ved ikk helt hvad input skal være til datetime
                    value = value.replace(" ", "T")

                    #Converts Date to DateTime
                    if "T" not in value:
                        value = value + "T00:00:00"
                    
                    return Literal(str(value), datatype=XSD.dateTime)
            case "string":
                if value == "":
                    return Literal(None, datatype=XSD.integer)
                else:
                    return Literal(str(value), datatype=XSD.string)
            case _:
                print("shit in Literal broke")
                print(data)
                return

    #Looks in "Mapping.txt" to find the correct name of a class based on the name of the column in the csv files
    def GetPartialURI(self, columnName):
        f = open("Mapping.txt", 'r')
        while True:
            line = f.readline()
            line = line.split(';')
            if line[0] == columnName:
                break
        f.close()
        return line[1].strip()