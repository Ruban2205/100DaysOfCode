# Program to find the largest of three numbers
print("\nRuban Gino Singh - Day2 of #100DaysOfCode")

print("\nFinding largest number!\n")

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if num1 >= num2 and num1 >= num3: 
    print(num1, " is greater!")
elif num2 >= num1 and num2 >= num3: 
    print(num2, " is greater!")
else: 
    print(num3, " is greater!")


# Calculate the factorial of a number using loop 
print("\nRuban Gino Singh - Day2 of #100DaysOfCode")

print("\nFactorial of a python number!\n")

userInput = int(input("Enter a number: "))
factorial = 1 

if userInput >= 1: 
    for i in range(1, userInput+1): 
        factorial = factorial * i
print("Factorial of the given number is: ", factorial)
