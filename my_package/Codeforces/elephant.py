x = int(input())
if x % 5 == 0:
    moves = x // 5
else:
    moves = (x // 5) + 1
print(moves)