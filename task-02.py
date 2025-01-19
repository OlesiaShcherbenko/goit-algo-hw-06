from collections import deque

# Step 1: Define DFS algorithm
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result  # Return as soon as a path is found
    
    path.pop()  # Backtrack if no path is found
    return None

# Step 2: Define BFS algorithm
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # Queue of paths

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        node = path[-1]  # Last node in the path

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # No path found

# Step 3: Use DFS and BFS on the graph
source = "Station A"
destination = "Station E"

# Run DFS and BFS
dfs_path = dfs(G, source, destination)
bfs_path = bfs(G, source, destination)

# Print the paths
print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)

# Explanation of the paths
if dfs_path and bfs_path:
    print("\nExplanation:")
    print("DFS explores as far as possible along each branch before backtracking. "
          "This often results in a path that might not be the shortest.")
    print("BFS explores all neighbors at the current depth level before moving to the next level. "
          "This guarantees the shortest path in an unweighted graph.")
else:
    print("One or both algorithms could not find a path.")