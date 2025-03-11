def checkIfListSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return 'Not a non-decreasing list!'
        else:
            return 'Non-decreasing list!'

arr = list(input('Enter list elements: ').split())
print(checkIfListSorted(arr))