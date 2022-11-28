import rdflib

class TripleGenerator:
    def __init__(self, namespace):
        self.namespace = namespace

    def Patient(self, line: str, graph: rdflib.Graph):
        #Her skal der stå ting
        return

    def PatientSubjectTriple(self, subject, predicate, object):
        self.graph.add((subject, predicate, object))
        return