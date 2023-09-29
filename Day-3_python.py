# Program to find if the given number is positive, negative or zero 
print("\nRuban Gino Singh - Day3 of #100DaysOfCode")

print("\nFinding +ve or -ve or 0\n")

number = int(input("Enter a number: "))

if number > 0:
    print(number, " is Positive!")
elif number < 0: 
    print(number, " is Negative!")
else: 
    print(number, " is Zero!")

# --------------------------------------------------------- #

# Program to convert String to lowercase
print("\nRuban Gino Singh - Day3 of #100DaysOfCode")

print("\nConvert String to Lowercase\n")

stringInput = input("Enter a string: ")
print("Lowercase string is: ", stringInput.lower())

# --------------------------------------------------------- #

# Program to Generate summ of all even numbers form 1 to 100 
print("\nRuban Gino Singh - Day3 of #100DaysOfCode")

print("\nGenerate sum of all even numbers from 1 to 100\n")

total = 0
for num in range(0, 100, 2):
    total += num
print("Sum of all even numbers from 1 to 100 is: ", total)

# --------------------------------------------------------- #

# Program to create a simple number guessing game 
print("\nRuban Gino Singh - Day3 of #100DaysOfCode")

print("\nProgram a number guessing game!\n")

import random

num = random.randrange(0, 10)
guess = int(input("Enter the number to guess: "))

while num != guess: 
    if guess < num: 
        print("Your number is too Low!!!")
        guess = int(input("Enter the number again: "))
    elif guess > num: 
        print("Your number is Too High!")
        guess = int(input("Enter the number again: "))
    else: 
        break 
print("You guessed it right!!")