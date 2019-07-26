from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
g = Graph()
f1 = r'C:\Users\Pedro\Documents\vocabs\legalEnts\CPOV\CPOV-AP-SCOT-v1\2019-07-26_legalEntitiesConceptScheme.v2.ttl'
f2 = r'C:\Users\Pedro\Documents\vocabs\legalEnts\CPOV\CPOV-AP-SCOT-v1\copv-ap-scot.2f.owl'

g.parse(f1, format='turtle')
print(len(g))

g.parse(f2, format='turtle')
print(len(g))

#print(g.serialize(format='turtle'))
qres = g.query(
    """SELECT ?a ?d
       WHERE {
          ?a a skos:Concept;
          skosxl:prefLabel ?b .
          ?b skosxl:literalForm ?c .
          ?d a owl:NamedIndividual ; rdfs:label ?c 
       }""")

#for row in qres:
#    print("%s prefLabel %s literalForm %s  individual %s" % row)
#print('................')

for row in qres:
    print("<%s> <http://xmlns.com/foaf/0.1/focus> <%s> ." % row)
