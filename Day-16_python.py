# Calculate the area of a rectangle using class and methods.
print("\nRuban Gino Singh - Day16 of #100DaysOfCode\n")

print("Python program to calculcate the area of a rectangle using class and methods.\n")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)

area = rectangle.calculate_area()
print(f"The area of the rectangle is {area} square units.")

# --------------------------------------------------------- #

# Find the longest word in a sentence.
print("\nRuban Gino Singh - Day16 of #100DaysOfCode\n")

print("Python program to find the longest word in a sentence\n")

def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

sentence = input("Enter a sentence: ")

longest_word = find_longest_word(sentence)
print(f"The longest word in the sentence is: {longest_word}")

# --------------------------------------------------------- #