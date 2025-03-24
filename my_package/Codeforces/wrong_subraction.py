n, k = map(int, input().split())
i = 1
while i <= k:
    if n % 10 != 0:
        n -= 1
    elif n % 10 == 0:
        n //= 10
    i += 1
print(n)