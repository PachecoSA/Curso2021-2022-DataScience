# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Na7I6v6R9vH42k88RmYIxQ7Gyu5nIpr9

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
from rdflib.namespace import FOAF
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
janeURI = ns.JaneSmith
g.add((janeURI, RDF.type, ns.Researcher))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# TO DO
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

fullName = Literal("Jane Smith")
given = Literal("Jane")
familyName = Literal("Smith")

g.add((janeURI, VCARD.FN, fullName))
g.add((janeURI, VCARD.Given, given))
g.add((janeURI, VCARD.Family, familyName))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO

g.add((ns.UPM, RDF.type, ns.University))  # UPM como tipo de University

relation = Namespace("http://www.aktors.org/ontology/portal#")


g.add((ns.JohnSmith, relation.worksFor, ns.UPM))
# Visualize the results
for s, p, o in g:
  print(s,p,o)