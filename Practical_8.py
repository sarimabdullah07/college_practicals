# Group D - Practical 2
# Pizza Delivery using Prim's Algorithm

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 2, 'C': 4, 'E': 2},
    'E': {'C': 5, 'D': 2}
}

print("Pizza Delivery Locations:")
for location in graph:
    print(location)

start = input("\nEnter Starting Location: ").upper()

if start not in graph:
    print("Invalid Location!")

else:
    visited = [start]
    total_cost = 0

    print("\nMinimum Spanning Tree:")

    while len(visited) < len(graph):

        min_cost = 999
        u = ''
        v = ''

        for vertex in visited:
            for neighbour in graph[vertex]:

                if neighbour not in visited:
                    cost = graph[vertex][neighbour]

                    if cost < min_cost:
                        min_cost = cost
                        u = vertex
                        v = neighbour

        visited.append(v)
        total_cost = total_cost + min_cost

        print(u, "->", v, ":", min_cost, "minutes")

    print("\nMinimum Total Travel Cost:", total_cost, "minutes")
