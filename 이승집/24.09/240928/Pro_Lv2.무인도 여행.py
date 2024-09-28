from collections import deque

maps = ["X591X", "X1X5X", "X231X", "1XXX1"]

N, M = len(maps), len(maps[0])

print(N, M)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = []

visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'X' or visited[i][j] == 1:
            continue

        stay = 0
        Q = deque([(i, j)])
        visited[i][j] = 1

        while Q:
            now_i, now_j = Q.popleft()
            stay += int(maps[now_i][now_j])

            for k in range(4):
                next_i = now_i + dx[k]
                next_j = now_j + dy[k]

                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and maps[next_i][
                    next_j] != 'X':
                    Q.append((next_i, next_j))
                    visited[next_i][next_j] = 1

        answer.append(stay)

if answer:
    answer.sort()
else:
    answer = [-1]

print(answer)
