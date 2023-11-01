# Calculate the greatest common divisor (GCD) of a list of numbers.
print("\nRuban Gino Singh - Day 36 of #100DaysOfCode\n")

print("Python program to Calculate the greatest common divisor (GCD) of a list of numbers\n")

import math

def find_gcd(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to calculate the GCD.")

    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = math.gcd(gcd_result, num)

    return gcd_result

numbers = [12, 18, 24, 36]

result = find_gcd(numbers)

print(f"The GCD of {numbers} is {result}")

# --------------------------------------------------------- #
