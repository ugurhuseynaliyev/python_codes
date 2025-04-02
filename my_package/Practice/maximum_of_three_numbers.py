def max_of_three(a, b, c):
    maximum = a
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
print(max_of_three(8, -4, 12))