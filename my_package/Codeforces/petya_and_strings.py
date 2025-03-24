st1 = input().lower()
st2 = input().lower()


ans = 0
for i in range(len(st1)):
    ascii_1 = ord(st1[i])
    ascii_2 = ord(st2[i])
    if ascii_1 > ascii_2:
        ans = 1
        break
    elif ascii_1 < ascii_2:
        ans = -1
        break
    else:
        continue
print(ans)