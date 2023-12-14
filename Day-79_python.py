# Implement Bubble Sort Algorithm
print("\nRuban Gino Singh - Day 79 of #100DaysOfCode\n")

print("Python program to implement Bubble Sort Algorithm.\n")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted array:", my_list)

# --------------------------------------------------------- #


# Implement Insertion sort Algorithm 
print("\nRuban Gino Singh - Day 79 of #100DaysOfCode\n")

print("Python program to implement Bubble Sort Algorithm.\n")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)

print("Sorted array:", my_list)

# --------------------------------------------------------- #


# Implement Merge Sort Algorithm 
print("\nRuban Gino Singh - Day 79 of #100DaysOfCode\n")

print("Python program to implement Bubble Sort Algorithm.\n")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half) 
        merge_sort(right_half)  

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

my_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(my_list)

print("Sorted array:", my_list)

# --------------------------------------------------------- #


# Implement Quick Sort Algorithm 
print("\nRuban Gino Singh - Day 79 of #100DaysOfCode\n")

print("Python program to implement Bubble Sort Algorithm.\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)

print("Sorted array:", sorted_list)

# --------------------------------------------------------- #