from rdflib import Graph, Namespace

g = Graph()

g.parse("Yoink.n3")

q = '''select ?Concept where {
    ?Concept ns1:hospital_org ?b .
    ?b foaf:name "Donna Fales" .
    } LIMIT 100'''

res = g.query(q)

for x in res:
    print(x)




# OurOnt = Namespace("Ontology/TEST_ONT.ttl")

# g = Graph(bind_namespaces="Ontology/TEST_ONT.ttl")





# g.serialize(destination="yeetz.ttl")