n = int(input())
exists_in_tram = 0
maximum_capacity = []
for i in range(1, n+1):
    exiting, entering = map(int, input().split())
    exists_in_tram = exists_in_tram - exiting + entering
    maximum_capacity.append(exists_in_tram)
print(max(maximum_capacity))