# Find the intersection of two lists without duplicates.
print("\nRuban Gino Singh - Day15 of #100DaysOfCode\n")

print("Python program to find the intersection of two lists without duplicates\n")

def find_intersection(list1, list2): 

    set1 = set(list1)
    set2 = set(list2)

    intersection = set1.intersection(set2)

    result = list(intersection)

    return result

list1 = []
list2 = []

list_len = int(input("Enter the list length: "))

for i in range(list_len): 
    item_list1 = int(input("Enter " + str(i+1) + " number to store in list1: "))
    list1.append(item_list1)

for j in range(list_len): 
    item_list2 = int(input("Enter "+ str(j+1) +" number to store in list2: "))
    list2.append(item_list2)

print("\nList 1: " + str(list1))
print("List 2: " + str(list2))

intersection_result = find_intersection(list1, list2)
print("\nIntersection without duplicates: ", intersection_result)

# --------------------------------------------------------- #

# Calculate the sum of the first N natural numbers.
print("\nRuban Gino Singh - Day15 of #100DaysOfCode\n")

print("Python program to calcualte the sum of the first N Natural Numbers\n")

def sum_of_first_n_numbers(num): 
    if num <= 0: 
        return "N must be a positive integer!"

    sum_n = (num * (num + 1)) // 2

    return sum_n

num = int(input("Enter a positive integer (N): "))
result = sum_of_first_n_numbers(num)

if type(result) == int: 
    print(f"The sum of first {num} natural numbers is: {result}")
else: 
    print(result)

# --------------------------------------------------------- #

# Create a program to reverse a sentence word by word
print("\nRuban Gino Singh - Day15 of #100DaysOfCode\n")

print("Python program to reverse a sentence word by word\n")

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
reversed_result = reverse_sentence(input_sentence)
print("Reversed sentence:", reversed_result)

# --------------------------------------------------------- #

# Check if a number is a perfect square.
print("\nRuban Gino Singh - Day15 of #100DaysOfCode\n")

print("Python program to check if a number is a perfect square\n")

import math

def is_perfect_square(number):
    if number < 0:
        return False
    
    square_root = int(math.sqrt(number))
    return square_root * square_root == number

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")

# --------------------------------------------------------- #