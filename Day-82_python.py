# Implement Cycle Sort Algorithm 
print("\nRuban Gino Singh - Day 82 of #100DaysOfCode\n")

print("Python program to Implement Cycle Sort Algorithm\n")

def cycle_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        item = arr[i]
        
        pos = i
        for j in range(i + 1, n):
            if arr[j] < item:
                pos += 1
                
        if pos == i:
            continue
        
        while item == arr[pos]:
            pos += 1
            
        arr[pos], item = item, arr[pos]
        
        while pos != i:
            pos = i
            for j in range(i + 1, n):
                if arr[j] < item:
                    pos += 1
                    
            while item == arr[pos]:
                pos += 1
                
            arr[pos], item = item, arr[pos]
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = cycle_sort(arr.copy())
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

# --------------------------------------------------------- #