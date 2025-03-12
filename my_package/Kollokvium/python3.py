def removeDuplicates(arr):
    new_arr = []
    for i in arr:
        if not(i in new_arr):
            new_arr.append(i)
    return new_arr

arr = list(input('Enter list elements: ').split())
print(removeDuplicates(arr))