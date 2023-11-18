# Implement the columnar cipher 
print("\nRuban Gino Singh - Day 53 of #100DaysOfCode\n")

print("Python program to implement the Column Transposition Cipher\n")

def encrypt(message, key):
    message = message.replace(" ", "")
    
    rows = len(message) // len(key)
    if len(message) % len(key) != 0:
        rows += 1
    
    padding = len(key) - len(message) % len(key)
    message += "X" * padding
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            if i * len(key) + j < len(message):
                row.append(message[i * len(key) + j])
            else:
                row.append("X")
        matrix.append(row)
    
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    ciphertext = ""
    for i in range(len(key)):
        for j in range(rows):
            ciphertext += matrix[j][column_order.index(i)]
    
    return ciphertext

def decrypt(ciphertext, key):
    rows = len(ciphertext) // len(key)
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            row.append("")
        matrix.append(row)
    
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    index = 0
    for i in range(len(key)):
        for j in range(rows):
            matrix[j][column_order[i]] = ciphertext[index]
            index += 1
    
    plaintext = ""
    for i in range(rows):
        for j in range(len(key)):
            plaintext += matrix[i][j]
    
    plaintext = plaintext.replace("X", "")
    
    return plaintext

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter key: ")
    
    ciphertext = encrypt(message, key)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {decrypt(ciphertext, key)}")

# --------------------------------------------------------- #