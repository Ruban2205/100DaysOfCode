# Implementation of a Bucket Sort Algorithm
print("\nRuban Gino Singh - Day 77 of #100DaysOfCode\n")

print("Python program to implement Bucket Sort Algorithm.\n")

def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)

    value_range = max_val - min_val

    num_buckets = len(arr)

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_val) / (value_range / (num_buckets - 1)))
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr

input_array = [3.4, 1.8, 0.5, 2.2, 5.1, 4.7]
sorted_array = bucket_sort(input_array)

print("Original array:", input_array)
print("Sorted array:", sorted_array)

# --------------------------------------------------------- #