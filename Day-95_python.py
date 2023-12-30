# Implement a python program to perform Hashing 
print("\nRuban Gino Singh - Day 95 of #100DaysOfCode.\n")

print("Python program to Implement Hashing.\n")

import hashlib

def hash_data(data, algorithm='sha256'):
    
    if isinstance(data, str):
        data = data.encode('utf-8')

    hash_object = hashlib.new(algorithm)

    hash_object.update(data)

    hashed_value = hash_object.hexdigest()

    return hashed_value

data_to_hash = "Hello, Hashing!"
hashed_result = hash_data(data_to_hash)

print(f"Original Data: {data_to_hash}")
print(f"Hashed Value: {hashed_result}")

# --------------------------------------------------------- #