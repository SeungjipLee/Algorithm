import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or arr[nx][ny]:
                continue

            arr[nx][ny] = 1
            q.append((nx,ny))
            cnt += 1

    return cnt


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if not arr[i][j]:
                arr[i][j] = 1
            
res = []
for i in range(m):
    for j in range(n):
        if not arr[i][j]:
            res.append(bfs(i,j))

res.sort()
print(len(res))
print(*res)