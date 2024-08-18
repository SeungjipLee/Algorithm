from collections import deque


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
n, m = len(maps), len(maps[0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Q = deque([(0, 0, 1)])
answer = 0

while Q:
    now_x, now_y, dist = Q.popleft()
    if now_x == n-1 and now_y == m-1:
        answer = dist
        break

    for i in range(4):
        next_x, next_y = now_x + dx[i], now_y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1:
            maps[next_x][next_y] = 2
            Q.append((next_x, next_y, dist + 1))
else:
    answer = -1

print(answer)