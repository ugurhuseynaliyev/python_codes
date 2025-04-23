def print_reverse(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        print_reverse(n-1)
print_reverse(5)