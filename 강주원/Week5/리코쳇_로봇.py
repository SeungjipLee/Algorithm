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
                nx = x + i[0]
                ny = y + i[1]
                if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] == 'D':
                    continue
                if i[0] == 1:
                    while 1:
                        if nx >= r or board[nx][ny] == 'D':
                            nx -= 1
                            break
                        nx += 1
                elif i[0] == -1:
                    while 1:
                        if nx < 0 or board[nx][ny] == 'D':
                            nx += 1
                            break
                        nx -= 1
                elif i[1] == 1:
                    while 1:
                        if ny >= c or board[nx][ny] == 'D':
                            ny -= 1
                            break
                        ny += 1
                elif i[1] == -1:
                    while 1:
                        if ny < 0 or board[nx][ny] == 'D':
                            ny += 1
                            break
                        ny -= 1
                if board[nx][ny] == 'G':
                    return cnt + 1
                
                if visit[nx][ny]:
                    continue

                visit[nx][ny] = 1
                q.append([nx,ny,cnt+1])

        return -1

    answer = bfs(x, y)
    return answer

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))