import networkx as nx

# Step 1: Add weights to the edges
# Define weighted edges (connection, weight)
weighted_connections = [
    ("Station A", "Station B", 4),
    ("Station B", "Station C", 2),
    ("Station C", "Station D", 3),
    ("Station D", "Station E", 6),
    ("Station A", "Station C", 5),  # Additional connection with a weight
]

# Create a new weighted graph
weighted_graph = nx.Graph()

# Add weighted edges to the graph
weighted_graph.add_weighted_edges_from(weighted_connections)

# Step 2: Implement Dijkstra's algorithm
# Find the shortest path between all pairs of nodes
shortest_paths = dict(nx.all_pairs_dijkstra_path(weighted_graph))
shortest_distances = dict(nx.all_pairs_dijkstra_path_length(weighted_graph))

# Print shortest paths and distances
print("Shortest Paths Between All Vertices:")
for start_node, paths in shortest_paths.items():
    for end_node, path in paths.items():
        print(f"{start_node} to {end_node}: Path = {path}")

print("\nShortest Distances Between All Vertices:")
for start_node, distances in shortest_distances.items():
    for end_node, distance in distances.items():
        print(f"{start_node} to {end_node}: Distance = {distance}")

# Step 3: Visualize the weighted graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(weighted_graph)  # Layout for visualization
nx.draw(
    weighted_graph,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
)
# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(weighted_graph, "weight")
nx.draw_networkx_edge_labels(weighted_graph, pos, edge_labels=edge_labels, font_size=10)
plt.title("Weighted City Subway Network", fontsize=14)
plt.show()