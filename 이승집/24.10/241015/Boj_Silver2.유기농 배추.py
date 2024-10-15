import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(s_n, s_m, N, M, board, visited):
    Q = deque([(s_n, s_m)])
    visited[s_n][s_m] = 1
    while Q:
        now_n, now_m = Q.popleft()
        for k in range(4):
            next_n = now_n + dx[k]
            next_m = now_m + dy[k]
            if 0 > next_n or N <= next_n or 0 > next_m or M <= next_m:
                continue
            if board[next_n][next_m] == 1 and not visited[next_n][next_m]:
                visited[next_n][next_m] = 1
                Q.append((next_n, next_m))


for tc in range(TC):
    M, N, B = map(int, input().split())
    cnt = 0
    board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in range(B):
        m, n = map(int, input().split())
        board[n][m] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j, N, M, board, visited)
                cnt += 1

    print(cnt)
