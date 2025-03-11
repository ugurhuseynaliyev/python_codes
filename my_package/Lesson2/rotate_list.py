def rotateList(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

list = input('Enter list elements: ').split()
k = int(input('Enter number of positions: '))
print(rotateList(list, k))
