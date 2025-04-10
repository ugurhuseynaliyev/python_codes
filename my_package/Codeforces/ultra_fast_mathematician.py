a = input()
b = input()
result = ''

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
print(result)
