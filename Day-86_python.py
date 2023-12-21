# Implement a pancake sorting algorithm.
print("\nRuban Gino Singh - Day 86 of #100DaysOfCode\n")

print("Python program to Implement Pancake sorting algorithm\n")

def flip(arr, i):
    """
    Helper function to flip the elements of the array up to index i.
    """
    start, end = 0, i
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def find_max_index(arr, n):
    """
    Helper function to find the index of the maximum element in the array.
    """
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """
    Pancake sorting algorithm implementation.
    """
    n = len(arr)
    for size in range(n, 1, -1):
        max_index = find_max_index(arr, size - 1)
        if max_index != size - 1:
            flip(arr, max_index)
            flip(arr, size - 1)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)
pancake_sort(arr)
print("Sorted array:", arr)

# --------------------------------------------------------- #