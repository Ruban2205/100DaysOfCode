# Calculate the difference between two dates.
print("\nRuban Gino Singh - Day19 of #100DaysOfCode\n")

print("Python program to calculate the difference between two dates\n")

from datetime import datetime

date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

try:
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please use the format 'YYYY-MM-DD'.")
else:
    date_difference = date2 - date1
    days_difference = date_difference.days
    print(f"The difference between the two dates is {days_difference} days.")

# --------------------------------------------------------- #

# Check if a list is a palindrome.
print("\nRuban Gino Singh - Day19 of #100DaysOfCode\n")

print("Python program to check if a list is a palindrome\n")

def is_palindrome(input_list):
    return input_list == input_list[::-1]

input_list = input("Enter a list of elements separated by spaces: ").split()

input_list = [int(item) if item.isdigit() else item for item in input_list]

if is_palindrome(input_list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# --------------------------------------------------------- #