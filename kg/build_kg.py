from rdflib import Graph, URIRef, Literal, Namespace
import pandas as pd

g = Graph()
ex = Namespace("http://example.org/")
g.bind("ex", ex)

courses = pd.read_csv("../data/courses.csv")

for _, row in courses.iterrows():
    course_uri = URIRef(ex + row["course_id"])
    g.add((course_uri, ex.title, Literal(row["title"])))
    for prereq in row["prerequisites"].split(","):
        if prereq:
            g.add((URIRef(ex + prereq), ex.prerequisiteOf, course_uri))

g.serialize("../kg/edu_kg.ttl", format="turtle")