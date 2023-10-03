# Finding prime number upto a given limit. 

print("Ruban Gino Singh - Day7 of #100DaysOfCode\n")

print("\nProgram to find a prime number upto a given\n")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def list_primes(limit):
    prime_list = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

try:
    limit = int(input("Enter the limit to list prime numbers up to: "))
    if limit < 2:
        print("Prime numbers start from 2.")
    else:
        primes = list_primes(limit)
        print("Prime numbers up to", limit, "are:", primes)
except ValueError:
    print("Please enter a valid positive integer.")

    