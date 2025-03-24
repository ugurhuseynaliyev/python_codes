s = input()
lowercase = 0
uppercase = 0
for i in s:
    if i == i.upper():
        uppercase += 1
    else:
        lowercase += 1
if uppercase > lowercase:
    print(s.upper())
elif uppercase < lowercase or uppercase == lowercase:
    print(s.lower())