import random # Needed to randomly generate the code
import string # Helpful to shortening the code

# Assigning variables to a string with 
letters = string.ascii_letters
numbers = string.digits
specialChars = string.punctuation

# Welcome Message
print("\nPassword Generator -> Generate your strong passwords here... :) \n")

# User Input. 
letterInput = int(input("How many letter you want?: "))
numbersInput = int(input("How many numbers you want?: "))
specialCharsInput = int(input("How many spcial characters you want?: "))

# Generating the password
password = ''
for i in range(letterInput): 
    password += random.choice(letters)
for i in range(numbersInput): 
    password += random.choice(numbers)
for i in range(specialCharsInput): 
    password += random.choice(specialChars)

# Mixing the strings. 
password = ''.join(random.sample(password, len(password)))

print("Recommended password: " + password)