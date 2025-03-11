def frequentElement(arr):
    count = 0
    number = arr[0]
    for i in arr:
        most_frequent = arr.count(i)
        if most_frequent > count:
            count = most_frequent
            number = i
    return number

arr = input('Enter list elements: ').split()
print(frequentElement(arr))