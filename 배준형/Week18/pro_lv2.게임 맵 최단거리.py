from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] > 0 or maps[nx][ny] == 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

    return visited[n-1][m-1]