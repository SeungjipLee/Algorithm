from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
res = set()

def bfs(x,y):
    q = deque()
    q.append([x,y,str(board[x][y]),1])
    while q:
        x, y, s, cnt = q.popleft()
        if cnt == 6:
            res.add(s)
            continue

        for i in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            ns = s + str(board[nx][ny])
            q.append([nx, ny, ns, cnt+1])
            

for i in range(5):
    for j in range(5):
        bfs(i,j)

print(len(res))