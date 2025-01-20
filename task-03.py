import heapq

# Step 1: Define the weighted graph as an adjacency list
weighted_connections = [
    ("Station A", "Station B", 4),
    ("Station B", "Station C", 2),
    ("Station C", "Station D", 3),
    ("Station D", "Station E", 6),
    ("Station A", "Station C", 5),
]

# Convert connections into an adjacency list
graph = {}
for u, v, w in weighted_connections:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  # Undirected graph

# Step 2: Implement Dijkstra's algorithm
def dijkstra(graph, start):
    # Initialize the distances dictionary and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    predecessors = {node: None for node in graph}  # For path reconstruction

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if this node's distance has already been optimized
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Step 3: Find shortest paths between all pairs of vertices
def find_all_shortest_paths(graph):
    all_paths = {}
    all_distances = {}

    for node in graph:
        distances, predecessors = dijkstra(graph, node)
        all_distances[node] = distances
        all_paths[node] = {}

        # Reconstruct paths from the predecessors
        for target in graph:
            if target == node:
                continue

            path = []
            current = target
            while current:
                path.append(current)
                current = predecessors[current]

            all_paths[node][target] = path[::-1]  # Reverse the path

    return all_distances, all_paths

# Compute shortest paths
all_distances, all_paths = find_all_shortest_paths(graph)

# Step 4: Display results
print("Shortest Distances Between All Vertices:")
for start, distances in all_distances.items():
    for end, distance in distances.items():
        print(f"Distance from {start} to {end}: {distance}")

print("\nShortest Paths Between All Vertices:")
for start, paths in all_paths.items():
    for end, path in paths.items():
        print(f"Path from {start} to {end}: {' -> '.join(path)}")