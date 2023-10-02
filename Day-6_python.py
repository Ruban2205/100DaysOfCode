# Check if a list is sorted in ascending order.
print("\nRuban Gino Singh - Day6 of #100DaysOfCode")

print("\nProgram to check if the list is sorted in ascending order\n")

list1 = []

list_len = int(input("Enter the length of the list: "))

for index_val in range(list_len):
    item = int(input("Enter the list items: "))
    list1.append(item)

print("Original List: ", list1)

flag = 0 

if(list1 == sorted(list1)): 
    flag = 1 

if (flag): 
    print("Yes, The list is sorted!!")
else: 
    print("No, The list is not sorted!!")

# --------------------------------------------------------- #

# Calculate the Greatest Common Divisor of Two numbers. 
print("\nRuban Gino Singh - Day6 of #100DaysOfCode")

print("\nProgram to find the GCD of two numbers\n")

import math 

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

gcd_result = math.gcd(num1, num2)

print("GCD of " + str(num1) + " and " + str(num2) + " is: " + str(gcd_result))

# --------------------------------------------------------- #