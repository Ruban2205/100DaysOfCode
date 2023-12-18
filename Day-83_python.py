# Implementation of Cocktail Sort Algorithm 
print("\nRuban Gino Singh - Day 83 of #100DaysOfCode\n")

print("Python Implementation of Cocktail Sorting algorithm\n")

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        swapped = False

        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False

        end = end-1

        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

cocktail_sort(arr)

print("Sorted array:", arr)

# --------------------------------------------------------- #