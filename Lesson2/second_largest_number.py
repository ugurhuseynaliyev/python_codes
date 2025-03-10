arr = list(input('Enter list elements: ').split(' '))
sorted_arr = []

def secondLargestNumber(arr):
    while arr:
        largest_number = arr[0]
        for num in arr:
            if num > largest_number:
                largest_number = num
        sorted_arr.append(largest_number)
        arr.remove(largest_number)
    return sorted_arr[1]


print(secondLargestNumber(arr))