# Find the index of the first occurrence of a character in a string.
print("\nRuban Gino Singh - Day5 of #100DaysOfCode")

print("\nProgram to find the first occurence of a char in a string.\n")

string_input = input("Enter the string: ")
to_find = input("Enter the input char to find: ")

print(string_input.find(to_find))

# --------------------------------------------------------- #

# Count number of words in a sentence 
print("Ruban Gino Singh - Day5 of #100DaysOfCode")

print("\nCount number of words in a sentence using python\n")

words_input = input("Enter the sentence: ").split()
lenOfWords = len(words_input)
print("Total length of the given sentence is: ", lenOfWords)

# --------------------------------------------------------- #

# Remove all vowels from a string
print("\nRuban Gino Singh - Day5 of #100DaysOfCode")

print("\nPython program to remove vowels from a string!\n")

def removeVowels(string): 
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print("String after removing vowels: ", result)

string = input("Enter the string: ")
removeVowels(string)