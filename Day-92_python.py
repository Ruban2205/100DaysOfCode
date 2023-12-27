# Implement Dijkstra's Algorithm 
print("\nRuban Gino Singh - Day 92 of #100DaysOfCode\n")

print("Python program to Implement Dijkstra's Algorithm.\n")

import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for (neighbor, weight) in graph.edges[current_node]:
            distance = current_distance + weight

            if neighbor not in visited:
                heapq.heappush(heap, (distance, neighbor))

    return visited

g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")

g.add_edge("A", "B", 1)
g.add_edge("A", "C", 3)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 4)
g.add_edge("C", "D", 1)

start_node = "A"
result = dijkstra(g, start_node)

print(f"Shortest paths from {start_node}: {result}")

# --------------------------------------------------------- #