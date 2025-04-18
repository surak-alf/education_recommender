from rdflib import Graph, URIRef, Literal, Namespace
import pandas as pd

def build_knowledge_graph():
    # Initialize KG
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    # Load synthetic data
    courses = pd.read_csv("../data/courses.csv")

    # Add courses and prerequisites to KG
    for _, row in courses.iterrows():
        course_uri = URIRef(ex + row["course_id"])
        g.add((course_uri, ex.title, Literal(row["title"])))
        
        # Handle prerequisites
        for prereq in row["prerequisites"].split(","):
            if prereq:
                g.add((URIRef(ex + prereq), ex.prerequisiteOf, course_uri))

    # Save KG
    g.serialize("../kg/edu_kg.ttl", format="turtle")
    print("Knowledge graph built and saved to 'kg/edu_kg.ttl'.")

if __name__ == "__main__":
    build_knowledge_graph()