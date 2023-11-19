from collections import deque

class Graph:
    def __init__(self, vertices, adjacency_list):
        self.vertices = vertices
        self.adjacency_list = adjacency_list

def bfs(graph, start):
    visited = [False] * graph.vertices
    queue = deque([start])
    visited[start] = True

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=' ')

        for neighbor in graph.adjacency_list[current_vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

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

# Perform BFS starting from vertex 0
print("BFS starting from vertex 0:")
bfs(graph, 0)
