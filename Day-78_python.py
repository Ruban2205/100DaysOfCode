# Imeplement Selection sort algorithm 
print("\nRuban Gino Singh - Day 78 of #100DaysOfCode\n")

print("Python implementation of a selection sort algorithm.\n")

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    print("Original List:", my_list)

    selection_sort(my_list)

    print("Sorted List:", my_list)

# --------------------------------------------------------- #