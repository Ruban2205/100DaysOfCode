# Find the longest subarray with a sum less than a given value.
print("\nRuban Gino Singh - Day 43 of #100DaysOfCode\n")

print("Python program to find the longest subarray with a sum less than a given value\n")

def find_longest_subarray(arr, target_sum):
    if not arr:
        return []

    max_len = 0
    max_subarray = []
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target_sum:
            current_sum -= arr[left]
            left += 1

        if (right - left + 1) > max_len:
            max_len = right - left + 1
            max_subarray = arr[left:right + 1]

    return max_subarray

arr = [1, 2, 3, 4, 5]
target_sum = 9
result = find_longest_subarray(arr, target_sum)
print("Longest subarray with sum less than", target_sum, "is:", result)

# --------------------------------------------------------- #