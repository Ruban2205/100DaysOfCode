# Count the number of even and odd elements in a list.
print("\nRuban Gino Singh - Day17 of #100DaysOfCode\n")

print("Python program to count the number of even and odd elements in a list\n")

def count_even_odd_elements(lst):
    even_count = 0
    odd_count = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

sample_list = []

list_len = int(input("Enter the length of the list: "))

for index in range(list_len): 
    item = int(input("Enter the " + str(index+1) + " number: "))
    sample_list.append(item)

print("Original list: " + str(sample_list))

even, odd = count_even_odd_elements(sample_list)
print("Number of even elements:", even)
print("Number of odd elements:", odd)

# --------------------------------------------------------- #

# Remove whitespace from the beginning and end of a string.
print("\nRuban Gino Singh - Day17 of #100DaysOfCode\n")

print("Python program to remove whitespace from the beginning and the end of the string\n")

def remove_whitespace(input_string):
    cleaned_string = input_string.strip()
    return cleaned_string

input_string = input("Enter a long string: ")
cleaned_string = remove_whitespace(input_string)
print("Original string:", input_string)
print("Cleaned string:", cleaned_string)

# --------------------------------------------------------- #