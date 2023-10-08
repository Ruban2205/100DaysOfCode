# Calculate the product of all elements in a list.
print("Ruban Gino Singh - Day12 of #100DaysOfCode\n")

print("\nProgram to calculate the product of all elements in a list.\n")

def multiply_number(list):
    prod = 1 
    for i in list: 
        prod = prod * i 
    return prod 

given_list = [] 

list_len = int(input("Enter the length of the list: "))

for index in range(list_len): 
    item = int(input("Enter the numbers: "))
    given_list.append(item)

print("\nOriginal List: ", given_list)
print("The product of the list is: ")
print(multiply_number(given_list))

# --------------------------------------------------------- #

# Convert a decimal number to binary using recursion.
print("Ruban Gino Singh - Day12 of #100DaysOfCode\n")

print("\nPython program to convert a decimal number to binary using recursion\n")

def getBinary(decimal_num): 
    if decimal_num == 0:
        return 0 
    
    result = getBinary(decimal_num // 2)
    return decimal_num % 2 + 10 * result 

decimal_num = int(input("Enter the decimal number: "))
print("The binary equivalent of " + str(decimal_num) + " is: " + str(getBinary(decimal_num)))

# --------------------------------------------------------- #