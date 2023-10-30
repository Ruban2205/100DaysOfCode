# Create a program to calculate compound interest.
print("\nRuban Gino Singh - Day 34 of #100DaysOfCode\n")

print("Python program to calculate a compund interest.\n")

def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return amount, interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = float(input("Enter the number of years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

final_amount, interest_earned = compound_interest(principal, rate, time, n)

print(f"Principal Amount: ${principal:.2f}")
print(f"Annual Interest Rate: {rate * 100:.2f}%")
print(f"Time (years): {time}")
print(f"Number of Times Compounded per Year: {n}")
print(f"Final Amount: ${final_amount:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")

# --------------------------------------------------------- #