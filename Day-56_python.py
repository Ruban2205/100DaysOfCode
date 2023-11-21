# To find a rank matrix of a given program
print("\nRuban Gino Singh - Day 56 of #100DaysOfCode\n")

print("\nPython program to Find the Rank matrix\n")

import numpy as np

def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

example_matrix = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

rank = matrix_rank(example_matrix)

print(f"The rank of the matrix is: {rank}")

# --------------------------------------------------------- #