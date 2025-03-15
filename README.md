
# Failure Mode and Effect Analysis (FMEA) for Financial Transactions

## Overview
This project performs **Failure Mode and Effect Analysis (FMEA)** on financial transactions using a **Neo4j graph database**. It identifies potential failure modes (e.g., high-value transactions, repeated transactions) and visualizes the results using Python libraries like **NetworkX** and **Matplotlib**.

---

## Objectives
1. **Identify Failure Modes**:
   - Detect high-value transactions, repeated transactions, and other anomalies.
2. **Visualize Transaction Data**:
   - Represent transactions as a graph and highlight failure modes.
3. **Generate a Report**:
   - Summarize the findings in a text file.

---

## Folder Structure
```
fmea_financial_transactions/
│
├── data/                       # Folder for datasets
│   └── transactions.csv        # Sample financial transaction dataset
│
├── scripts/                    # Folder for Python scripts
│   ├── data_loader.py          # Load data into Neo4j
│   ├── graph_constructor.py    # Build the graph
│   ├── fmea_analyzer.py        # Perform FMEA analysis
│   └── visualizer.py           # Visualize the graph
│
├── output/                     # Folder for output files
│   ├── graph_visualization.png # Graph visualization image
│   └── fmea_report.txt         # Summary report of FMEA findings
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Setup Instructions

### Prerequisites
1. **Neo4j Desktop**:
   - Download and install [Neo4j Desktop](https://neo4j.com/download/).
   - Create a new database and note the credentials (username: `neo4j`, password: `password`).

2. **Python**:
   - Install Python 3.x from [python.org](https://www.python.org/).

3. **Python Libraries**:
   - Install the required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Contents of `requirements.txt`:
     ```
     neo4j
     pandas
     networkx
     matplotlib
     ```

---

## How to Run the Project

1. **Load Data into Neo4j**:
   - Run the `data_loader.py` script to load the CSV data into Neo4j:
     ```bash
     python scripts/data_loader.py
     ```

2. **Construct the Graph**:
   - Run the `graph_constructor.py` script to build the transaction graph:
     ```bash
     python scripts/graph_constructor.py
     ```

3. **Perform FMEA Analysis**:
   - Run the `fmea_analyzer.py` script to identify failure modes:
     ```bash
     python scripts/fmea_analyzer.py
     ```

4. **Visualize the Graph**:
   - Run the `visualizer.py` script to generate the graph visualization:
     ```bash
     python scripts/visualizer.py
     ```

5. **Check Output**:
   - The output will be saved in the `output/` folder:
     - `graph_visualization.png`: Graph visualization image.
     - `fmea_report.txt`: Summary report of failure modes.

---

## Example Output

### Graph Visualization
- Nodes represent transactions.
- Red nodes represent failure modes (e.g., high-value transactions).
- Blue nodes represent normal transactions.

### FMEA Report
```
FMEA Analysis Report
====================
Transaction ID: 3, Amount: 15000.0, Failure Mode: High-value transaction
Transaction ID: 2, Amount: 5000.0, Failure Mode: Repeated transaction
```

---

## Tools and Technologies
- **Neo4j**: Graph database for storing and querying transaction data.
- **Python**: For data processing, FMEA analysis, and visualization.
- **Pandas**: For handling CSV data.
- **NetworkX and Matplotlib**: For graph visualization.
- **Cypher Query Language**: For interacting with Neo4j.

---

## Challenges
1. **Setting up Neo4j**:
   - Resolved by following Neo4j documentation and tutorials.
2. **Defining Failure Modes**:
   - Researched common fraud patterns to define meaningful failure modes.
3. **Visualization**:
   - Focused on a subset of data to manage computational load.

---

## Future Improvements
1. Add more failure modes (e.g., transactions from unknown senders).
2. Enhance visualization with interactive tools like **Plotly**.
3. Integrate real-time transaction data for live analysis.

---

## Author
[NAKKA JAGADEESH]  
[21eg112c31@anurag.edu.in]  


---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

