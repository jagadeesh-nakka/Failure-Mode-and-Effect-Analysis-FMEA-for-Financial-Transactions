from py2neo import Graph, Relationship

# Connect to Neo4j

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Medha@2020"))

# Query transactions
query = """
MATCH (t1:Transaction), (t2:Transaction)
WHERE t1.timestamp < t2.timestamp AND t1.sender_id = t2.sender_id
CREATE (t1)-[:NEXT_TRANSACTION]->(t2)
"""
graph.run(query)

print("Graph constructed successfully!")