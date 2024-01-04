# Implement a Travelling Salesman Problem
print("\nRuban Gino Singh - It's Day 100 of #100DaysOfCode\n")

print("Python program to Implement a Travelling salesman problem.\n")

from itertools import permutations

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]] 
    return total_distance

def traveling_salesman_bruteforce(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    optimal_path = None

    for path in permutations(cities):
        current_distance = calculate_total_distance(path, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_path = path

    return optimal_path, min_distance

if __name__ == "__main__":

    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    optimal_path, min_distance = traveling_salesman_bruteforce(distances)

    print("Optimal Path:", optimal_path)
    print("Minimum Distance:", min_distance)

# --------------------------------------------------------- #