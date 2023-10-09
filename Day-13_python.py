# Check if a string contains only alphabetic characters.
print("\nRuban Gino Singh - Day13 of #100DaysOfCode\n")

print("Program to check if a string contains only alphabetic characters\n")

string_input = input("Enter the string: ")

if string_input.isalpha(): 
    print("It contains only alphabetic characters!")
else: 
    print("It contains numbers! It's not a perfect alphabetic characters!")
    
# --------------------------------------------------------- #

# Calculate the LCM (Least Common Multiple) of two numbers.
print("\nRuban Gino Singh - Day13 of #100DaysOfCode\n")

print("Program to calculate the LCM of two numbers\n")

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

def lcm(a, b): 
    max_num = max(a, b)
    while True: 
        if max_num % a == 0 and max_num % b == 0: 
            return max_num
        max_num += 1

print("LCM of the given two number is: " + str(lcm(num1, num2)))

# --------------------------------------------------------- #

# Implement a basic calculator with addition and subtraction
print("\nRuban Gino Singh - Day13 of #100DaysOfCode\n")

print("Program to Implement a basic calculator with addition and subtraction\n")

def add_num(a, b): 
    return a + b

def sub_num(a, b): 
    return a - b

while True: 
    print("Choose the operation (1 or 2): ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))
    
    
    if choice == 1: 
        num1 = int(input("Enter the number1: "))
        num2 = int(input("Enter the number2: "))
        print("\nThe Addition result is: " + str(add_num(num1, num2)) + "\n")
    elif choice == 2: 
        num1 = int(input("Enter the number1: "))
        num2 = int(input("Enter the number2: "))
        print("\nThe Subtraction result is: " + str(sub_num(num1, num2)) + "\n")
    elif choice == 3: 
        break
    else: 
        print("Invalid Choice Entered!!!")

# --------------------------------------------------------- #