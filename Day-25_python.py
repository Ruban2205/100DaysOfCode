# Check if a string is an anagram of another string.
print("\nRuban Gino Singh - Day 25 of the #100DaysOfCode\n")

print("Python program to check if a string is an anagram of another string.\n")

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count1 = {}
    char_count2 = {}

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    return char_count1 == char_count2

string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
if result:
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

# --------------------------------------------------------- #

# Find the longest increasing subarray in a list.
print("\nRuban Gino Singh - Day 25 of #100DaysOfCode\n")

print("Program to find the longest increasing subarray in a list.\n")

def find_longest_increasing_subarray(arr):
    if not arr:
        return []

    current_subarray = [arr[0]]
    longest_subarray = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_subarray.append(arr[i])
        else:
            if len(current_subarray) > len(longest_subarray):
                longest_subarray = current_subarray
            current_subarray = [arr[i]]

    if len(current_subarray) > len(longest_subarray):
        longest_subarray = current_subarray

    return longest_subarray

arr = [1, 2, 3, 2, 3, 4, 5, 1, 2, 3, 4, 5]
result = find_longest_increasing_subarray(arr)
print("Longest increasing subarray:", result)


# --------------------------------------------------------- #

# Calculate the median of a list of numbers.
print("\nRuban Gino Singh - Day 25 of #100DaysOfCode\n")

print("Python program to calculate the median of a list of numbers.\n")

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1: 
        median = sorted_numbers[n // 2]
    else:  
        middle1 = sorted_numbers[(n - 1) // 2]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2

    return median

numbers = [5, 2, 9, 1, 5, 6]
median = calculate_median(numbers)
print("Median:", median)

# --------------------------------------------------------- #
