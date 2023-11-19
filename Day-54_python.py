# Create a program to convert between different numeral systems (e.g., binary to decimal).
print("\nRuban Gino Singh - Day 54 of #100DaysOfCode\n")

print("Create a python program to convert between different numeral systems!\n")

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def main():
    print("Numeral System Converter")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        decimal_input = int(input("Enter a decimal number: "))
        binary_result = decimal_to_binary(decimal_input)
        print(f"Binary representation: {binary_result}")

    elif choice == "2":
        binary_input = input("Enter a binary number: ")
        decimal_result = binary_to_decimal(binary_input)
        print(f"Decimal representation: {decimal_result}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

# --------------------------------------------------------- #