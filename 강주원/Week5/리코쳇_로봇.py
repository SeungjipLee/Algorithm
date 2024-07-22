from collections import deque

def solution(board):
    r = len(board)
    c = len(board[0])
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                x, y = i, j
    
    visit = [[0] * c for _ in range(r)]
    def bfs(x, y):
        q = deque([(x,y,0)])
        visit[x][y] = 1
        while q:
            x, y, cnt = q.popleft()
            for i in [(1,0), (0,1), (-1,0), (0,-1)]:
                xx, yy = x, y
                while 1:
                    nx = xx + i[0]
                    ny = yy + i[1]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] == 'D':
                        break
                    xx = nx
                    yy = ny

                if board[xx][yy] == 'G':
                    return cnt + 1
                
                if visit[xx][yy]:
                    continue

                visit[xx][yy] = 1
                q.append([xx,yy,cnt+1])

        return -1

    answer = bfs(x, y)
    return answer
