# Swap the values of two variables using tuple packing and unpacking.
print("\nRuban Gino Singh - Day8 of #100DaysOfCode")

print("\nProgram to swap the values of two variables using tuple packing and unpacking\n")

a = int(input("Enter the first number to store in (a): "))
b = int(input("Enter the second number to store in (b): "))

a, b = b, a

print("a =", a)
print("b =", b) 

# --------------------------------------------------------- #

# Calculate the power of a number using a loop.
print("Ruban Gino Singh - Day8 of #100DaysOfCode")

print("\nProgram to calculcate the power of a number using a loop.\n")

num = int(input("Enter the number: "))
power = int(input("Enter the power value: "))

count = 1
for i in range(power):
    count = count * num

print("Powers of the given number is: ", count)

# --------------------------------------------------------- #

# Find the second smallest number in a list.
print("Ruban Gino Singh - Day8 of #100DaysOfCode\n")

print("\nProgram to find the second smallest number is a list.\n")

def second_smallest(list1):
    return sorted(set(list1))[1]

list1 = []

list_range = int(input("Enter the list range: "))

for index in range(list_range):
    item = int(input("Enter the number: "))
    list1.append(item)

print("\nOriginal list: ", list1)

print("\nSecond smallest number from the original list is: ", second_smallest(list1))

# --------------------------------------------------------- #