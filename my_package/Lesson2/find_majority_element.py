def frequentElement(arr):
    count = 0
    number = arr[0]
    n = len(arr)
    for i in arr:
        most_frequent = arr.count(i)
        if most_frequent > count:
            count = most_frequent
            number = i
    if count > n // 2:
        return number
    else:
        return 'No majority element'

arr = input('Enter list elements: ').split()
print(frequentElement(arr))