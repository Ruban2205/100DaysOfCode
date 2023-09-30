# Calculate length of a string wihtout using built-in functions 
print("\nRuban Gino Singh - Day4 of #100DaysOfCode")

print("\nProgram to count number of strings without using built in functions\n")

string = input("Enter the string: ")
count = 0

for i in string: 
    count += 1

print("Total length of the string is: ", count)

# --------------------------------------------------------- #

# Reverse a list using Slicing 
print("\nRuban Gino Singh - Day4 of #100DaysOfCode")

print("\nReverse a list using slicing\n")

numbers = []

list_len = int(input("Enter the list length: "))

for index_val in range(list_len): 
    list_item = int(input("Enter the list numbers: "))
    numbers.append(list_item)

print("Original list is: ", numbers)
print("Reversed list is: ", numbers[::-1])

# --------------------------------------------------------- #

# Check whether the given number is palindrome without using loop 
print("\nRuban Gino Singh - Day4 of #100DaysOfCode")

print("\nCheck if a string is palindrome without using loops\n")

num = input("Enter the number: ")
try: 
    value = int(num)
    if num == str(num)[::-1]: 
        print(num, " is a palindrome!")
    else: 
        print(num, " is not a palindrome!")
except ValueError: 
    print("\nGiven input is not a valid number!!!\n")

# --------------------------------------------------------- #

# Calculate the average of a list of numbers 
print("\nRuban Gino Singh - Day4 of #100DaysOfCode")

print("\nCalculate the average of a list of numbers\n")

def avgList(list1): 
    return sum(list1) / len(list1)

list1 = []
lst_length = int(input("Enter the list length: "))

for lst_index in range(lst_length): 
    lst_item = int(input("Enter the " + str(lst_index) + " item: "))
    list1.append(lst_item)

average = avgList(list1)

print("Given list is: ", list1)
print("Average of given list is: ", round(average, 2))

# --------------------------------------------------------- #