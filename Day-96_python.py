# Python Implementation for Greedy Algorithm for Coin Change
print("\nRuban Gino Singh - Day 96 of #100DaysOfCode\n")

print("Python program to Implement a Greedy Algorithm for Coin Change.\n")

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)  

    num_coins = 0
    remaining_amount = amount

    for coin in coins:
        if remaining_amount >= coin:
            num_coins += remaining_amount // coin
            remaining_amount %= coin

    if remaining_amount == 0:
        return num_coins
    else:
        return -1  

coin_denominations = [25, 10, 5, 1]
change_amount = 63

result = greedy_coin_change(coin_denominations, change_amount)

if result != -1:
    print(f"Minimum number of coins needed for {change_amount} cents: {result}")
else:
    print("Exact change is not possible with the given coin denominations.")

# --------------------------------------------------------- #