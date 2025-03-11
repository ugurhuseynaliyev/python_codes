flatten_arr = [[1, 2, [3, 4]], [5, 6], 7]

def flatten(lst):
    flat_list = []
    for a in lst:
        if isinstance(a, list):
            flat_list.extend(flatten(a))
        else:
            flat_list.append(a)
    return flat_list
print(flatten(flatten_arr))