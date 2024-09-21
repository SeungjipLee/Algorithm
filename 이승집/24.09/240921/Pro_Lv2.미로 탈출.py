from collections import deque

maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
# maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]

"""
S : 시작점
E : 출구
L : 레버
O : 통로
X : 벽

1. 출발점 -> 레버
2. 레버 -> 도착점

두 과정은 visited를 따로 둬야한다.
최소거리이므로 visited대신 inf를 둬서 다익스트라처럼 풀어야하나
"""

answer = 0

N = len(maps)
M = len(maps[0])

START = (0, 0)
LEVER = (0, 0)
EXIT = (0, 0)

for i in range(N):
    for j in range(M):
        if maps[i][j] == "S":
            START = (i, j)
        elif maps[i][j] == "L":
            LEVER = (i, j)
        elif maps[i][j] == "E":
            EXIT = (i, j)


def bfs(start, target):
    visited = [[-1] * M for _ in range(N)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while queue:
        x, y, step = queue.popleft()
        if maps[x][y] == target:
            return step
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    visited[nx][ny] = step + 1
                    queue.append((nx, ny, step + 1))
    return -1


dist1 = bfs(START, 'L')
if dist1 == -1:
    print(answer)

else:
    dist2 = bfs(LEVER, 'E')
    if dist2 == -1:
        print(answer)
    else:
        answer = dist1 + dist2
        print(answer)
