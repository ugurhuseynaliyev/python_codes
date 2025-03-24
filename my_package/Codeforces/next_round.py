n, k = map(int, input().split())
scores = list(map(int, input().split()))

advancers = 0

kth_score = scores[k - 1]

for score in scores:
    if score >= kth_score and score > 0:
        advancers += 1

print(advancers)