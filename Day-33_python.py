# Calculate the Hamming distance between two strings.
print("\nRuban Gino Singh - Day 33 of #100DaysOfCode\n")

print("Python program to calculate the hamming distance between two strings.\n")

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    distance = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance

string1 = "Rubang"
string2 = "Rubaan"
distance = hamming_distance(string1, string2)
print(f"The Hamming distance between '{string1}' and '{string2}' is {distance}")

# --------------------------------------------------------- #