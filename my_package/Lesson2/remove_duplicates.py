arr = list(input('Enter array elements: ').split(' '))
new_arr = []

def removeDuplicates(arr):
    for i in arr:
        if not(i in new_arr):
            new_arr.append(i)
    return new_arr

print(removeDuplicates(arr))
