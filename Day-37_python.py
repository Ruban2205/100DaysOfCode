# Create a program to simulate a dice roll.
print("\nRuban Gino Singh - Day 37 of #100DaysOfCode\n")

print("Python program to simulate a dice roll.\n")

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()

# --------------------------------------------------------- #