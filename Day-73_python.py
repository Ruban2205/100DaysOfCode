# Build a blockchain with basic transaction functionality.
print("\nRuban Gino Singh - Day 73 of #100DaysOfCode\n")

print("Python program to build a blockchain with basic transaction functionality\n")

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash_value = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash_value)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

def add_transaction(sender, recipient, amount):
    data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    block_data = f"Transaction: {data}"
    new_block = create_new_block(previous_block, block_data)
    blockchain.append(new_block)
    return new_block

add_transaction("Alice", "Bob", 10.0)
add_transaction("Bob", "Charlie", 5.0)

for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print("\n")
    previous_block = block

# --------------------------------------------------------- #