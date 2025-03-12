def listIsSorted(arr):
    for i in range(1, len(arr)): # 1 2 3
        if arr[i] > arr[i-1]:
            return 'Non-decreasing order!'
        return 'Not a non-decrasing order!'
arr = list(input('Enter list elements: '))
print(listIsSorted(arr))