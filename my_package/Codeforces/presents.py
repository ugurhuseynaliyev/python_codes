n = int(input())
friends = list(map(int, input().split()))
givers = [0] * n

for giver in range(n):
    receiver = friends[giver]
    givers[receiver - 1] = giver + 1
print(' '.join(map(str, givers)))