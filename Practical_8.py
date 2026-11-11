
# Group D - Practical 2
# Pizza Delivery using Prim's Algorithm

# Weighted Graph
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 2, 'C': 4, 'E': 2},
    'E': {'C': 5, 'D': 2}
}

# Prim's Algorithm
def prim(start):
    visited = set()
    visited.add(start)

    total_cost = 0
    mst = []

    while len(visited) < len(graph):

        min_cost = float('inf')
        selected_edge = None

        for vertex in visited:
            for neighbour, cost in graph[vertex].items():

                if neighbour not in visited:
                    if cost < min_cost:
                        min_cost = cost
                        selected_edge = (vertex, neighbour)

        if selected_edge is None:
            print("Graph is not connected!")
            return

        u, v = selected_edge

        visited.add(v)
        mst.append((u, v, min_cost))
        total_cost += min_cost

    print("\nMinimum Spanning Tree:")
    for u, v, cost in mst:
        print(u, "->", v, ":", cost, "minutes")

    print("\nMinimum Total Travel Cost:", total_cost, "minutes")

# Main Program
print("Pizza Delivery Locations:")
for location in graph:
    print(location)

start = input("\nEnter Starting Location: ").upper()

if start in graph:
    prim(start)
else:
    print("Invalid Location!")
