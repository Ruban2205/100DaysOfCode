# Check if a string follows a specific pattern (e.g., ABABAB).
print("\nRuban Gino Singh - Day 27 of the #100DaysOfCode\n")

print("Check if a string follows a specific pattern\n")

def follows_pattern(s, pattern):
    parts = s.split(pattern)
    
    if len(parts) != 3:
        return False
    
    if parts[0] == parts[1] == parts[2]:
        return True
    
    return False

input_string = input("Enter a string: ")
pattern = "ABABAB"

if follows_pattern(input_string, pattern):
    print(f'The string "{input_string}" follows the pattern "{pattern}".')
else:
    print(f'The string "{input_string}" does not follow the pattern "{pattern}".')


# --------------------------------------------------------- #