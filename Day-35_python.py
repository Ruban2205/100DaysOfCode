# Find the shortest path in a graph using Breadth-First Search (BFS).
print("\nRuban Gino Singh - Day 35 of #100DaysOfCode\n")

print("Python program to find the shortest path in a graph using Breadth-First Search (BFS)\n")

from collections import defaultdict, deque 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list)

    def add_edge(self, u, v): 
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end): 
        if start == end: 
            return [start]
        
        visited = set()
        queue = deque()
        parent = {}
        found = False

        queue.append(start)
        visited.add(start)

        while queue: 
            current = queue.popleft()

            for neighbor in self.graph[current]: 
                if neighbor not in visited: 
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current 

                    if neighbor == end: 
                        found = True 
                        break 

        if not found: 
            return []
        
        path = [end]

        while end != start: 
            end = parent[end]
            path.insert(0, end)
        
        return path
    
if __name__ == "__main__": 
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('C', 'F')
    g.add_edge('F', 'G')
    g.add_edge('E', 'G')

    start_node = 'A'
    end_node = 'G'
    shortest_path = g.shortest_path(start_node, end_node)

    if shortest_path:
        print(f"Shortest Path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path found from {start_node} to {end_node}")


# --------------------------------------------------------- #