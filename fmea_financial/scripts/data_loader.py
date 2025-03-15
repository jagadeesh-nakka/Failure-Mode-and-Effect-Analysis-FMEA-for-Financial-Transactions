from py2neo import Graph, Node
import pandas as pd

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Medha@2020"))

# Load CSV data
df = pd.read_csv("data/transactions.csv")

# Create transaction nodes in Neo4j
for _, row in df.iterrows():
    tx = Node("Transaction",
              transaction_id=row['transaction_id'],
              amount=row['amount'],
              type=row['type'],
              timestamp=row['timestamp'],
              sender_id=row['sender_id'],
              receiver_id=row['receiver_id'])
    graph.create(tx)

print("Data loaded into Neo4j successfully!")