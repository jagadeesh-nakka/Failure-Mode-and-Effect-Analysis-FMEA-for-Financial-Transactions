from py2neo import Graph

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Medha@2020"))

# Define failure modes
def detect_failure_modes():
    # High-value transactions
    high_value_query = """
    MATCH (t:Transaction)
    WHERE t.amount > 10000
    SET t.failure_mode = 'High-value transaction'
    RETURN t
    """
    graph.run(high_value_query)

    # Repeated transactions
    repeated_query = """
    MATCH (t1:Transaction)-[:NEXT_TRANSACTION]->(t2:Transaction)
    WHERE t1.sender_id = t2.sender_id AND t1.amount = t2.amount AND duration.between(t1.timestamp, t2.timestamp).minutes < 10
    SET t1.failure_mode = 'Repeated transaction', t2.failure_mode = 'Repeated transaction'
    RETURN t1, t2
    """
    graph.run(repeated_query)
    
def generate_report():
    query = """
    MATCH (t:Transaction)
    WHERE t.failure_mode IS NOT NULL
    RETURN t.transaction_id AS id, t.amount AS amount, t.failure_mode AS failure_mode
    """
    results = graph.run(query).data()

    with open("output/fmea_report.txt", "w") as f:
        f.write("FMEA Analysis Report\n")
        f.write("===================\n")
        for result in results:
            f.write(f"Transaction ID: {result['id']}, Amount: {result['amount']}, Failure Mode: {result['failure_mode']}\n")

generate_report()
print("Report generated successfully!")

detect_failure_modes()
print("FMEA analysis completed!")