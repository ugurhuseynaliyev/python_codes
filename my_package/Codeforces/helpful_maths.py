s = input()
arr = []
for i in s:
    if i != '+':
        if i == '1' or i == '2' or i == '3':
            arr.append(i)
arr.sort()
result = '+'.join(map(str,arr))
print(result)