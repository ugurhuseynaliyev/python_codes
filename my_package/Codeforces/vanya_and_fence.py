n, h = map(int, input().split())
road_width = 0
height_of_friends = list(map(int, input().split()))

if n == len(height_of_friends):
    for i in height_of_friends:
        if i > h:
            road_width += 2
        else:
            road_width += 1
print(road_width)