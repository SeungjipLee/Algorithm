import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    if visit[x][y] or not Map[x][y]:
        return 0
    
    visit[x][y] = 1
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
            nx = x + i[0]
            ny = y + i[1]
            if nx >= h or nx < 0 or ny >= w or ny < 0 or visit[nx][ny] or not Map[nx][ny]:
                continue
            q.append([nx,ny])
            visit[nx][ny] = 1

    return 1

while 1:
    w, h = map(int, input().split())
    visit = [[0]*w for _ in range(h)]
    if not w and not h:
        break
    
    res = 0
    Map = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
           res += bfs(i,j) 

    print(res)