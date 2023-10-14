# Find the index of the last occurrence of a character in a string.
print("\nRuban Gino Singh - Day 18 of #100DaysOfCode\n")

print("Python program to find the index of the last occurrence of a character in a string\n")

def find_last_occurrence(string, char):
    index = string.rfind(char)
    if index != -1:
        return index
    else:
        return "Character not found in the string"

def find_last_occurrence_manually(string, char):
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i
    return "Character not found in the string"

input_string = input("Enter the string: ")
search_char = input("Enter the character to search: ")

result_rfind = find_last_occurrence(input_string, search_char)
print(f"Using rfind(): The last occurrence of '{search_char}' is at index {result_rfind}")

result_manual = find_last_occurrence_manually(input_string, search_char)
print(f"Using manual iteration: The last occurrence of '{search_char}' is at index {result_manual}")

# --------------------------------------------------------- #

# Implement a basic command-line calculator with multiple operations.
print("\nRuban Gino Singh - Day18 of #100DaysOfCode\n")

print("Python program to Implement a basic command-line calculator with multiple operations\n")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")

# --------------------------------------------------------- #