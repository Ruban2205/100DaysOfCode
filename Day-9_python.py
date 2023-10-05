# Remove duplicates from a list without changing the order.
print("Ruban Gino Singh - Day9 of #100DaysOfCode\n")

print("\nPython program to remove duplicates from a list without changing order\n")

list1 = []

list_length = int(input("Enter the length of list: "))

for index in range(list_length):
    item = int(input("Enter the number: "))
    list1.append(item)

print("\nOriginal list: " + str(list1) + "\n")

list1 = list(set(list1))

print("\nThe list after removing duplicates: " + str(list1))

# --------------------------------------------------------- #

# Calculate the area of a circle using the radius.
print("Ruban Gino Singh - Day9 of #100DaysOfCode\n")

print("\nPython program to calculate the area of circle using the radius.\n")

radius = int(input("Enter the radius value: "))

area_of_circle = 3.14 * radius * radius

print("\nArea of the Circle is: " + str(area_of_circle))

# --------------------------------------------------------- #