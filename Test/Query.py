from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("test.ttl")

sparql.setQuery('select ?Concept where {?Concept rdfs:label "Yeet"@en} LIMIT 100')

res = sparql.query()

print(res)