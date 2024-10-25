from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
answer = 0
visited = [0] * n
Q = deque([])

for i in range(n):
    if visited[i] == 0:
        answer += 1
        visited[i] = 1
        Q.append(i)
        while Q:
            now = Q.popleft()
            for j in range(n):
                if j != now and computers[now][j] == 1 and visited[j] == 0:
                    Q.append(j)
                    visited[j] = 1
print(answer)