from collections import deque

def solution(board):
    
    answer = 0
    n, m = len(board), len(board[0])
    
    visited = [[0] * m for _ in range(n)]
    q = deque()
    
    s, e = -1, -1
    gs, ge = -1, -1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                s = i
                e = j
            elif board[i][j] == 'G':
                gs = i
                ge = j
    q.append([s, e])
    visited[s][e] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            a, b = x, y
            while True:
                nx, ny = a+dx, b+dy
                if nx < 0 or ny < 0 or nx >= n or ny >=m or board[nx][ny] =="D":
                    break
                a, b = nx, ny
            # if visited[a][b] != 0 and visited[a][b] > visited[x][y] + 1:
            if visited[a][b]:
                continue
            visited[a][b] = visited[x][y] + 1
            q.append([a, b])
    print(visited)
    answer = visited[gs][ge]-1

    return answer