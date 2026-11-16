
# Group D - Practical 1
# BFS and DFS Graph Traversal

vertices = ['A', 'B', 'C', 'D', 'E']

matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

# DFS Traversal
visited = set()
stack = ['A']

print("DFS Traversal:")

while stack:
    vertex = stack.pop()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        index = vertices.index(vertex)

        for i in range(len(vertices)-1, -1, -1):
            if matrix[index][i] == 1:
                next_vertex = vertices[i]

                if next_vertex not in visited:
                    stack.append(next_vertex)

# BFS Traversal
visited = set()
queue = ['A']

visited.add('A')

print("\n\nBFS Traversal:")

while queue:
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

print()
