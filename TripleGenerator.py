import rdflib

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

    def GetClassURI(self, classTuple):
        classColumnName, classID = classTuple
        return rdflib.URIRef(str("http://www.example.com/" + self.GetPartialURI(classColumnName) + "/" + classID))

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
            case _:
                print("yoooo, shit broke in GetPredicateURI")
                print(name)
                return

    def LavTriple(self, subject, object, predicate):
        self.graph.add((self.GetClassURI(subject), self.GetPredicateURI(predicate), self.GetClassURI(object)))



    def GetPartialURI(self, columnName):
        f = open("Mapping.txt", 'r')
        while True:
            line = f.readline()
            line = line.split(';')
            if line[0] == columnName:
                break
        f.close()
        return line[1].strip()