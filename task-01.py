import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a graph
G = nx.Graph()

# Define nodes (subway stations)
stations = ["Station A", "Station B", "Station C", "Station D", "Station E"]

# Add nodes to the graph
G.add_nodes_from(stations)

# Define edges (connections between stations)
connections = [
    ("Station A", "Station B"),
    ("Station B", "Station C"),
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    ("Station A", "Station C"),
]

# Add edges to the graph
G.add_edges_from(connections)

# Step 2: Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    font_size=12,
    font_weight="bold",
    edge_color="gray",
)
plt.title("City Subway Network", fontsize=14)
plt.show()

# Step 3: Analyze the graph's characteristics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print("Graph Characteristics:")
print(f"Number of nodes (stations): {num_nodes}")
print(f"Number of edges (connections): {num_edges}")
print("Degree of each node (connections per station):")
for station, degree in degrees.items():
    print(f"  {station}: {degree}")