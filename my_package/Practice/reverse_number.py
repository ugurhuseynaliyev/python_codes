def reverse_number(n):
    s = ''
    while n > 0:
        k = n % 10
        s += str(k)
        n = n // 10
    return s
print(reverse_number(1234))