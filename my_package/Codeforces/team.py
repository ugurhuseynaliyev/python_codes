n = int(input())
ans = 0

for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    petya = lst[0]
    vasya = lst[1]
    tonya = lst[2]
    total = petya + vasya + tonya
    if total >= 2:
        ans += 1
    else:
        continue

print(ans)