class Graph:
    def __init__(self, vertices, adjacency_list):
        self.vertices = vertices
        self.adjacency_list = adjacency_list

def dfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True

    for neighbor in graph.adjacency_list[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def depth_first_search(graph, start):
    visited = [False] * graph.vertices
    dfs(graph, start, visited)

# Example Usage:
# Define a graph with 6 vertices and an adjacency list
vertices = 6
adjacency_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Create a Graph object
graph = Graph(vertices, adjacency_list)

# Perform DFS starting from vertex 0
print("DFS starting from vertex 0:")
depth_first_search(graph, 0)
