# Calculate the covariance between two lists of numbers.
print("\nRuban Gino Singh - Day 45 of #100DaysOfCode\n")

print("Python program to calculate the covariance between two lists of numbers.\n")

def calculate_covariance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")

    mean_list1 = sum(list1) / len(list1)
    mean_list2 = sum(list2) / len(list2)

    covariance = sum((list1[i] - mean_list1) * (list2[i] - mean_list2) for i in range(len(list1))) / (len(list1) - 1)

    return covariance

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

covariance_result = calculate_covariance(list1, list2)
print(f"Covariance between list1 and list2: {covariance_result}")

# --------------------------------------------------------- #