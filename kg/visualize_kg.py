from rdflib import Graph
from pyvis.network import Network
import pandas as pd

def visualize_kg():
    # Load the KG
    g = Graph()
    g.parse("./kg/edu_kg.ttl", format="turtle")

    # Create a PyVis network
    net = Network(height="750px", width="100%", notebook=True, directed=True)
    
    # Add nodes and edges
    nodes = set()
    for s, p, o in g:
        if "prerequisiteOf" in str(p):
            nodes.add(str(s))
            nodes.add(str(o))
            net.add_node(str(s), label=str(s).split("/")[-1], color="#FFA07A")
            net.add_node(str(o), label=str(o).split("/")[-1], color="#98FB98")
            net.add_edge(str(s), str(o), label="prerequisiteOf", color="#808080")

    # Save and show
    net.show("./kg/kg_visualization.html", notebook=False)
    print("KG visualization saved to 'kg/kg_visualization.html'. Open in a browser.")

if __name__ == "__main__":
    visualize_kg()