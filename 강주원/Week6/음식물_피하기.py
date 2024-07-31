import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
hall = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    hall[a-1][b-1] = 1

visit = [[0]*m for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] or not hall[nx][ny]:
                continue

            cnt += 1
            visit[nx][ny] = 1
            q.append((nx,ny))
    
    return cnt

res = 0
for i in range(n):
    for j in range(m):
        if hall[i][j] and not visit[i][j]:
            res = max(res, bfs(i,j))

print(res)