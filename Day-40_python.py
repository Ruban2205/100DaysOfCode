# Calculate the edit distance between two strings (Levenshtein distance).
print("\nRuban Gino Singh - Day 40 of #100DaysOfCode\n")

print("Python program to calculate the edit distance between two strins (levenshtein distance)\n")

def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,   
                dp[i][j - 1] + 1,     
                dp[i - 1][j - 1] + substitution_cost  
            )

    return dp[m][n]

str1 = "kitten"
str2 = "sitting"
distance = levenshtein_distance(str1, str2)
print(f"Levenshtein distance between '{str1}' and '{str2}' is {distance}")

# --------------------------------------------------------- #