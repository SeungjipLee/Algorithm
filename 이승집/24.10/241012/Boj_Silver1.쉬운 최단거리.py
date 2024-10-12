import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
answer = [[-1] * M for _ in range(N)]
sx, sy = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            answer[i][j] = 0
        elif board[i][j] == 2:
            sx, sy = i, j
            answer[i][j] = 0

Q = deque([(sx, sy)])

while Q:
    now_x, now_y = Q.popleft()
    for k in range(4):
        next_x = now_x + dx[k]
        next_y = now_y + dy[k]
        if (0 <= next_x < N) and (0 <= next_y < M) and (answer[next_x][next_y] == -1) and (board[next_x][next_y] == 1):
            answer[next_x][next_y] = answer[now_x][now_y] + 1
            Q.append((next_x, next_y))

for row in answer:
    print(*row)