# Find the longest subsequence of a string in alphabetical order.
print("\nRuban Gino Singh - Day 58 of #100DaysOfCode\n")

print("Python program to find Longest Subsequence of a string in alphabetical order.\n")

def longest_alphabetical_subsequence(s):
    if not s:
        return ""

    current_subsequence = s[0]
    longest_subsequence = s[0]

    for char in s[1:]:
        if ord(char) >= ord(current_subsequence[-1]):
            current_subsequence += char
        else:
            current_subsequence = char

        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence

    return longest_subsequence

input_string = "abcabcdefgxyz"
result = longest_alphabetical_subsequence(input_string)
print(f"The longest alphabetical subsequence is: {result}")

# --------------------------------------------------------- #