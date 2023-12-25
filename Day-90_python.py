# Implement a Depth First Search Algorithm 
print("\nRuban Gino Singh - Day 90 of #100DaysOfCode\n")

print("Python program to Implement a Depth First Search Algorithm\n")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()

        def dfs_recursive(node):
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    print("Depth First Traversal starting from node 1:")
    g.dfs(1)

# --------------------------------------------------------- #