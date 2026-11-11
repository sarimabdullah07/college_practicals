
# Group D - Practical 1
# BFS and DFS Graph Traversal

from collections import deque

vertices = ['A', 'B', 'C', 'D', 'E']

# Adjacency Matrix for DFS
matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

# Adjacency List for BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

# DFS using Adjacency Matrix
def DFS(start):
    visited = set()

    def dfs_visit(vertex):
        index = vertices.index(vertex)
        visited.add(vertex)

        print(vertex, end=" ")

        for i in range(len(vertices)):
            if matrix[index][i] == 1:
                next_vertex = vertices[i]

                if next_vertex not in visited:
                    dfs_visit(next_vertex)

    dfs_visit(start)

# BFS using Adjacency List
def BFS(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main Program
print("Graph Vertices:", vertices)

print("\nDFS Traversal:")
DFS('A')

print("\n\nBFS Traversal:")
BFS('A')

print()
