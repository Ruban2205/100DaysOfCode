# Implementation of Binary Search
print("\nRuban Gino Singh - Day 88 of #100DaysOfCode\n")

print("Python program to Implement Binary Search Algorithm\n")

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid 
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")

# --------------------------------------------------------- #