def product_list(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product_list(arr[1:])
print(product_list([2,3,4]))