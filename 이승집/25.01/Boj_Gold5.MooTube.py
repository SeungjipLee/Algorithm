import sys
from collections import deque


input = sys.stdin.readline
N, Q = map(int, input().split())
Board = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    Board[a].append((b, c))
    Board[b].append((a, c))

for _ in range(Q):
    visited = [0] * (N + 1)
    standard, start = map(int, input().split())
    cnt = 0
    Q = deque([start])
    visited[start] = 1
    while Q:
        now = Q.popleft()
        for i, j in Board[now]:
            if visited[i] == 0 and j >= standard:
                cnt += 1
                Q.append(i)
                visited[i] = 1
    print(cnt)