# Calculate the determinant of a square matrix.
print("\nRuban Gino Singh - Day 61 of #100DaysOfCode\n")

print("Python program to calculate the determinant of a square matrix\n")

import numpy as np

def calculate_determinant(matrix):
    try:
        np_matrix = np.array(matrix, dtype=float)
        
        if np_matrix.shape[0] != np_matrix.shape[1]:
            raise ValueError("The matrix must be square.")
        
        determinant = np.linalg.det(np_matrix)
        
        return determinant
    except Exception as e:
        return str(e)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = calculate_determinant(matrix)

if isinstance(result, float):
    print(f"The determinant of the matrix is: {result}")
else:
    print(f"Error: {result}")


# --------------------------------------------------------- #