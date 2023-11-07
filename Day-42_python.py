# Check if a number is a palindrome in binary representation.
print("\nRuban Gino Singh - Day 42 of #100DaysOfCode\n")

print("Python program to check if a number is a palindrome in binary representation\n")

def is_binary_palindrome(num):
    binary_str = bin(num)[2:]
    return binary_str == binary_str[::-1]

num = int(input("Enter a number:"))

if is_binary_palindrome(num):
    print(f"{num} is a binary palindrome.")
else:
    print(f"{num} is not a binary palindrome.")

# --------------------------------------------------------- #