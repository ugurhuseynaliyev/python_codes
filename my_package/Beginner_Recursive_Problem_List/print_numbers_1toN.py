def print_to_n(n):
    if n == 0:
        return
    else:
        print_to_n(n-1)
        print(n, end=' ')
print_to_n(5)