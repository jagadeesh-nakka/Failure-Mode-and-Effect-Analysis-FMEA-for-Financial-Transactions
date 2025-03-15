from py2neo import Graph
import networkx as nx
import matplotlib.pyplot as plt

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Medha@2020"))

# Query the graph
query = """
MATCH (t:Transaction)
RETURN t.transaction_id AS id, t.amount AS amount, t.failure_mode AS failure_mode
"""
data = graph.run(query).data()

# Create a NetworkX graph
G = nx.Graph()
for node in data:
    G.add_node(node['id'], amount=node['amount'], failure_mode=node['failure_mode'])

# Draw the graph
pos = nx.spring_layout(G)
node_colors = ['red' if G.nodes[node]['failure_mode'] else 'lightblue' for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray')
plt.savefig("output/graph_visualization.png")
plt.show()