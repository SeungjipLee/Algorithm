n = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(n)]

pillars.sort()

max_height = max(pillars, key=lambda x: x[1])[1]
max_height_index = next(i for i, pillar in enumerate(pillars) if pillar[1] == max_height)

area = 0
current_height = pillars[0][1]
for i in range(max_height_index):
    if pillars[i][1] > current_height:
        current_height = pillars[i][1]
    area += current_height * (pillars[i + 1][0] - pillars[i][0])

current_height = pillars[-1][1]
for i in range(len(pillars) - 1, max_height_index, -1):
    if pillars[i][1] > current_height:
        current_height = pillars[i][1]
    area += current_height * (pillars[i][0] - pillars[i - 1][0])

area += max_height

print(area)
