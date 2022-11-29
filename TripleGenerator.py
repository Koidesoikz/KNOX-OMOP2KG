import rdflib

class TripleGenerator:
    def __init__(self, namespace, graph):
        self.namespace = namespace
        self.graph = graph

    def GetGraph(self):
        return self.graph

    def SetGraph(self, graph):
        self.graph = graph

    def LavTriple(subject, object, predicate):
        #Det er ikke så simpelt, desværre
        #self.graph.add(subject, predicate, object)
        line = subject + " " + predicate + " " + object
        print(line)

    def Patient(self, line: str, graph: rdflib.Graph):
        #Her skal der stå ting
        return

    def PatientSubjectTriple(self, subject, predicate, object):
        self.graph.add((subject, predicate, object))
        return