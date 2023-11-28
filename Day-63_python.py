# Calculate the shortest path in a maze using Depth-First Search (DFS)
print("\nRuban Gino Singh - Day 63 of #100DaysOfCode\n")

print("Python program to Calculate the shortest path in a maze using Depth-First Search (DFS)\n")

def is_valid_move(maze, visited, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '.' and not visited[row][col]

def dfs(maze, visited, start, end, path):
    row, col = start

    visited[row][col] = True

    if start == end:
        return True
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        if is_valid_move(maze, visited, new_row, new_col):
            path.append((new_row, new_col))

            if dfs(maze, visited, (new_row, new_col), end, path):
                return True

            path.pop()

    return False

def find_shortest_path(maze):
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        print("Start or end not found in the maze.")
        return

    visited = [[False] * len(maze[0]) for _ in range(len(maze))]

    path = [start]

    if dfs(maze, visited, start, end, path):
        print("Shortest Path:")
        for position in path:
            print(position)
    else:
        print("No path found.")

maze = [
    "S..#.",
    "..###",
    "...#.",
    "E.#..",
    "....."
]

find_shortest_path(maze)

# --------------------------------------------------------- #