n = int(input())
responses = list(map(int, input().split()))

if n == len(responses):
    if 1 in responses:
        print('HARD')
    else:
        print('EASY')