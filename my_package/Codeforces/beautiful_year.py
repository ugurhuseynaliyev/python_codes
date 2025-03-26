n = input()
n = str(int(n)+1)
while True:
    if len(str(n)) != len(set(str(n))):
        n = int(n) + 1
    else:
        print(n)
        break