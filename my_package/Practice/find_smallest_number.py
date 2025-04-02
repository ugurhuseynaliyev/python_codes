def find_smallest_number(lst):
    smallest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest
print(find_smallest_number([-35, -20, 15, -30]))