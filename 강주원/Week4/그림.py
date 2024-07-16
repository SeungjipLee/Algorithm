import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
visit = [[0] * c for _ in range(r)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or visit[nx][ny] or not arr[nx][ny]:
                continue
            visit[nx][ny] = 1
            q.append([nx,ny])

    return cnt

res = []
for i in range(r):
    for j in range(c):
        if not visit[i][j] and arr[i][j]:
            res.append(bfs(i, j))

print(len(res))
if len(res):
    print(max(res))
else:
    print(0)