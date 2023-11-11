# Find the maximum sum subarray in a list using Kadane's algorithm.
print("\nRuban Gino Singh - Day 46 of #100DaysOfCode\n")

print("Python program to find the maximum sum subarray in a list using Kadane's algorithm\n")

def kadane_algorithm(arr):
    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

if __name__ == "__main__":
    input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = kadane_algorithm(input_list)

    print(f"The maximum sum subarray is: {max_sum}")

# --------------------------------------------------------- #