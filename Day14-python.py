# Find the mode (most frequent element) in a list.
print("\nRuban Gino Singh - Day 14 of #100DaysOfCode\n")

print("Python program to find the most frequent element in a list\n")

list1 = [] 

list_len = int(input("Enter the length of a list: "))

for index in range(list_len):
    item = int(input("Enter the numbers: "))
    list1.append(item)

print("The given list: ", str(list1))

def most_frequent(list1): 
    counter = 0
    num = list1[0]

    for i in list1: 
        curr_frequency = list1.count(i)
        if(curr_frequency > counter): 
            counter = curr_frequency
            num = i 
    return num 

print("The most frequent number in a list: ", most_frequent(list1))

# --------------------------------------------------------- #

# Calculate the square of each element in a list using list comprehension.
print("\nRuban Gino Singh - Day 14 of #100DaysOfCode\n")

print("Python program to calculate the square of each element in a list using list comprehension\n")

input_str = input("Enter a list of numbers separated by spaces: ")

numbers = [float(x) for x in input_str.split()]

squares = [x ** 2 for x in numbers]

print("Squares of the elements:", squares)

# --------------------------------------------------------- #

# Check if a string has balanced parentheses using a stack.
print("\nRuban Gino Singh - Day 14 of #100DaysOfCode\n")

print("Python program to check if a string has balanced parantheses using a stack")

def is_balanced_parentheses(s):
    stack = []
    
    parentheses_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_mapping.values():
            stack.append(char)

        elif char in parentheses_mapping.keys():
            if not stack:
                return False  
            top_element = stack.pop()
            if parentheses_mapping[char] != top_element:
                return False  

    return len(stack) == 0

string_1 = input("Enter the combination of brackets: ")

print("The string balanced: " + str(is_balanced_parentheses(string_1)))  
