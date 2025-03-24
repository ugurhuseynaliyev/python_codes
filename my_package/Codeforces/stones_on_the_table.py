n = int(input())
s = input()
neighboring = 0
if len(s) == n:
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            neighboring += 1
print(neighboring)
