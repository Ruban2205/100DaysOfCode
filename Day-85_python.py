# Implementation of Bitonic Sort Algorithm
print("\nRuban Gino Singh - Day 85 of #100DaysOfCode\n")

print("Python Implementation of Bitonic Sorting Algorithm\n")

def bitonic_sort(arr, direction):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    first_half = arr[:mid]
    second_half = arr[mid:]

    first_half = bitonic_sort(first_half, not direction)
    second_half = bitonic_sort(second_half, direction)

    bitonic_merge(arr, direction)

    return arr

def bitonic_merge(arr, direction):
    if len(arr) > 1:
        bitonic_compare(arr, direction)
        mid = len(arr) // 2
        bitonic_merge(arr[:mid], direction)
        bitonic_merge(arr[mid:], direction)

def bitonic_compare(arr, direction):
    distance = len(arr) // 2
    for i in range(distance):
        if (arr[i] > arr[i + distance]) == direction:
            arr[i], arr[i + distance] = arr[i + distance], arr[i]

if __name__ == "__main__":
    input_array = [3, 7, 4, 8, 6, 2, 1, 5]
    direction = True  

    print("Original array:", input_array)
    sorted_array = bitonic_sort(input_array, direction)
    print("Sorted array:", sorted_array)

# --------------------------------------------------------- #