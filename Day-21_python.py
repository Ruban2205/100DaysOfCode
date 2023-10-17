# Create a program to find the longest common prefix in a list of strings.
print("\nRuban Gino Singh - Day21 of #100DaysOfCode\n")

print("Python program to find the longest common prefix in a list of strings.\n")

def longest_common_prefix(strings):
    if not strings:
        return ""

    shortest = min(strings, key=len)
    
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]
    
    return shortest

string_list = ["flower", "flour", "flourish", "flourishing"]
result = longest_common_prefix(string_list)
if result:
    print("The longest common prefix is:", result)
else:
    print("There is no common prefix.")

# --------------------------------------------------------- #

# Calculate the area of a trapezoid.
print("\nRuban Gino Singh - Day21 of #100DaysOfCode\n")

print("Python program to calculate the area of a trapezoid\n")

def trapezoid_area(a, b, h):
    area = (1/2) * (a + b) * h
    return area

a = float(input("Enter the length of the first base (a): "))
b = float(input("Enter the length of the second base (b): "))
h = float(input("Enter the height (h): "))

area = trapezoid_area(a, b, h)
print("The area of the trapezoid is:", area)

# --------------------------------------------------------- #