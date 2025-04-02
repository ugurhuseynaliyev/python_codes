def sum_of_digits(n):
    s = 0
    while n > 0:
        k = n % 10
        s += k
        n //= 10
    return s
print(sum_of_digits(256))