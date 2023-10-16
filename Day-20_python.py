# Calculate the sum of all prime numbers from 1 to 100.
print("\nRuban Gino Singh - Day20 of #100DaysOfCode\n")

print("Python program to Calculate the sum of all prime numbers from 1 to 100\n")

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def sum_primes(limit):
    total = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            total += num
    return total

limit = 100
result = sum_primes(limit)
print(f"The sum of all prime numbers from 1 to {limit} is: {result}")

# --------------------------------------------------------- #

# Generate a random password of a specified length.
print("\nRuban Gino Singh - Day20 of #100DaysOfCode\n")

print("Python program to Generate a random password of a specified length\n")

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the length of a password to be generated: "))

random_password = generate_password(password_length)
print(f"Random Password: {random_password}")

# --------------------------------------------------------- #