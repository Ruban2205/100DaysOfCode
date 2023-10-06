# Check if a given year is a leap year using function
print("Ruban Gino Singh - Day10 of #100DaysOfCode\n")

print("\nProgram to check a given year is a leap year or not\n")

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400==0):
        print("The year is a leap year!")
    else:
        print("The year isn't a leap year!")

year = int(input("Enter the year: "))
leap_year(year)

# --------------------------------------------------------- #

# Find the sum of the digits of a number using recursion.
print("Ruban Gino Singh - Day10 of #100DaysOfCode\n")

print("\nProgram to find the sum of the digits of a number using recursion.\n")

def sum_of_digits(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    rest_of_digits = n // 10
    return last_digit + sum_of_digits(rest_of_digits)

num = int(input("Enter a number: "))

result = sum_of_digits(num)
print("The sum of the digits of", num, "is", result)
