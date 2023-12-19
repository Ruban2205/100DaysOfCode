# Implement Strand Sort Algorithm
print("\nRuban Gino Singh - Day 84 of #100DaysOfCode\n")

print("Python program to Implement Strand Sort Algorithm\n")

def strand_sort(arr):
    result = []

    while arr:
        sublist = [arr.pop(0)]

        i = 0
        while i < len(arr):
            if arr[i] > sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1

        result = merge(result, sublist)

    return result

def merge(list1, list2):
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_array = strand_sort(arr)

print("Sorted array:", sorted_array)

# --------------------------------------------------------- #