n = int(input())
rooms = 0

for i in range(n):
    p, q = map(int, input().split())
    if p + 2 <= q:
        rooms += 1
print(rooms)