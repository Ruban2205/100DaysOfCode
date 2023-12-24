# Implement a Breadth First Search algorithm 
print("\nRuban Gino Singh - Day 89 of #100DaysOfCode\n")

print("Python program to Implement Breadth First Search (BFS) Algorithm\n")

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        result = []

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                result.append(current_vertex)
                visited.add(current_vertex)
                queue.extend(self.graph[current_vertex])

        return result

if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_edge(0, [1, 2])
    my_graph.add_edge(1, [2])
    my_graph.add_edge(2, [0, 3])
    my_graph.add_edge(3, [3])

    start_vertex = 2
    bfs_result = my_graph.bfs(start_vertex)

    print(f"BFS starting from vertex {start_vertex}: {bfs_result}")

# --------------------------------------------------------- #