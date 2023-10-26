# Find the nth term in the Fibonacci sequence using memoization.
print("\nRuban Gino Singh - Day 30 of #100DaysOfCode\n")

print("Python program to find the nth term in the Fib")

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result

n = int(input("Enter the value of n: "))

result = fib(n)

print(f"The {n}th Fibonacci number is: {result}")

# --------------------------------------------------------- #