# Create a program to perform matrix addition and subtraction.
print("\nRuban Gino Singh - Day 41 of #100DaysOfCode\n")

print("Python program to perform a matrix addition and subtraction\n")

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for addition."
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for subtraction."
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

print("\nMatrix Addition:")
result_addition = add_matrices(matrix1, matrix2)
if isinstance(result_addition, list):
    print_matrix(result_addition)

print("\nMatrix Subtraction:")
result_subtraction = subtract_matrices(matrix1, matrix2)
if isinstance(result_subtraction, list):
    print_matrix(result_subtraction)

# --------------------------------------------------------- #