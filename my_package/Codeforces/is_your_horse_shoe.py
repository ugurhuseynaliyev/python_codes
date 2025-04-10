a = list(map(int, input().split()))
b = set(a)
if len(a) == 1:
    print(len(a) - 1)
else:
    print(len(a) - len(b))