# Implement a Counting Sort Algorithm
print("\nRuban Gino Singh - Day 81 of #100DaysOfCode\n")

print("Python program to Implement a Counting Sort Algorithm\n")

def counting_sort(arr):
    max_element = max(arr)
    
    count = [0] * (max_element + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_array = []
    for i in range(len(count)):
        sorted_array.extend([i] * count[i])
    
    return sorted_array

input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)

print("Original Array:", input_array)
print("Sorted Array:", sorted_array)

# --------------------------------------------------------- #