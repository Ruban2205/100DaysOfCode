# Create a program to sort a list of strings by length.
print("\nRuban Gino Singh - Day23 of #100DaysOfCode\n")

print("Python program to sort a list of strings by length\n")


def sort_strings_by_length(string_list):
    sorted_list = sorted(string_list, key=len)
    return sorted_list


if __name__ == "__main__":
    my_strings = ["apple", "banana", "cherry", "date", "fig"]

    sorted_strings = sort_strings_by_length(my_strings)

    print("Original List:", my_strings)
    print("Sorted List by Length:", sorted_strings)

# --------------------------------------------------------- #

# Calculate the dot product of two vectors represented as lists.

print("\nRuban Gino Singh - Day23 of #100DaysOfCode\n")

print("Python program to calcualte the dot product of two vectors represented as lists.\n")


def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError(
            "Vectors must have the same length for the dot product.")

    result = sum(x * y for x, y in zip(vector1, vector2))
    return result


if __name__ == "__main__":
    vector1 = [2, 4, 6]
    vector2 = [1, 3, 5]

    result = dot_product(vector1, vector2)

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Dot Product:", result)

# --------------------------------------------------------- #
