import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
max_size = 0
visited = [[0]*m for _ in range(n)]
Q = deque([])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            Q.append((i, j))
            cnt += 1
            mid = 1
            while Q:
                ni,nj = Q.popleft()
                for k in range(4):
                    nxi = ni + dx[k]
                    nxj = nj + dy[k]
                    if (0 <= nxi < n) and (0 <= nxj < m) and board[nxi][nxj] == 1 and visited[nxi][nxj] == 0:
                        Q.append((nxi, nxj))
                        visited[nxi][nxj] = 1
                        mid += 1
            max_size = max(mid, max_size)

print(cnt)
print(max_size)