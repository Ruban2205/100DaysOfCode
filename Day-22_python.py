# Find the smallest common multiple of multiple numbers.
print("\nRuban Gino Singh - Day22 of #100DaysOfCode\n")

print("Python program to find the smallest common multiple of multiple numbers\n")

import math 

def find_lcm(x, y):
    return x * y // math.gcd(x, y)

def find_lcm_multiple(numbers):
    if len(numbers) < 2: 
        return None 
    
    lcm = numbers[0]

    for i in range(1, len(numbers)):
        lcm = find_lcm(lcm, numbers[i])

    return lcm 

numbers = [] 

list_len = int(input("Enter the length of the list: "))

for index in range(list_len): 
    item = int(input("Enter the " + index + " number: "))
    numbers.append(item)

result = find_lcm_multiple(numbers)

if result is not None: 
    print(f"The LCM of {numbers} is {result}")
else: 
    print("LCM is undefined for fewer than two numbers")

# --------------------------------------------------------- #
 
# Implement a basic file encryption and decryption program.
print("\nRuban Gino Singh - Day22 of #100DaysOfCode\n")

print("Python program to Implement a basic file encryption and decryption program.\n")

def encrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                byte = f_in.read(1)
                if not byte:
                    break
                encrypted_byte = ord(byte) ^ key
                f_out.write(bytes([encrypted_byte]))

def decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                byte = f_in.read(1)
                if not byte:
                    break
                decrypted_byte = ord(byte) ^ key
                f_out.write(bytes([decrypted_byte]))

input_file = 'input.txt'
output_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'
encryption_key = 42

encrypt(input_file, output_file, encryption_key)
print(f'File encrypted and saved as {output_file}')

# Decrypt the file
decrypt(output_file, decrypted_file, encryption_key)
print(f'File decrypted and saved as {decrypted_file}')

# --------------------------------------------------------- #