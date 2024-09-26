from collections import deque

field = [list(input()) for _ in range(12)]


def bfs(x, y, color):
    visit[x][y] = 1
    q = deque([[x, y]])
    cnt = 1
    boom = [[x,y]]
    while q:
        x, y = q.popleft()
        for i in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6 or visit[nx][ny] or color != field[nx][ny]:
                continue

            cnt += 1
            visit[nx][ny] = 1
            q.append([nx,ny])
            boom.append([nx,ny])
    
    if cnt < 4:
        boom = []    
    return boom


def boom(arr):
    for r, c in arr:
        field[r][c] = '.'
        

def gravity(arr):
    # 각 열을 독립적으로 확인
    for col in range(6):
        empty_row = 11  # 제일 아래 행을 빈 공간으로 설정
        for row in range(11, -1, -1):
            if arr[row][col] == '.':
                continue

            arr[empty_row][col] = arr[row][col]
            if empty_row != row:
                arr[row][col] = '.'
            empty_row -= 1


chain = 0
while 1:
    visit = [[0]*6 for _ in range(12)]
    boom_list = []
    cnt = 0
    for i in range(12):
        for j in range(6):
            if field[i][j] == '.' or visit[i][j]:
                continue
            
            boom_ = bfs(i, j, field[i][j])
            if boom_:
                boom_list.extend(boom_)
                cnt += 1

    if cnt == 0:
        break

    boom(boom_list)
    gravity(field)
    chain += 1

print(chain)

'''
......
......
.Y....
.B....
.B....
.B....
.G....
.G..Y.
.B....
.YBBY.
.YBBY.
.YBBB.
'''