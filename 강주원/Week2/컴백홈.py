import sys
from collections import deque
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visit = [[0] * c for _ in range(r)]
res = 0

def sol(x,y,depth):
    global res
    if depth == k:
        if x == 0 and y == c-1:
            res += 1
        return
    visit[x][y] = 1

    for i in [(0,1), (1,0), (-1,0), (0,-1)]:
        nx = x + i[0]
        ny = y + i[1]
        if 0 > nx or 0 > ny or r <= nx or c <= ny or visit[nx][ny] or arr[nx][ny] == 'T':
            continue
        visit[nx][ny] = 1
        sol(nx,ny,depth+1)
        visit[nx][ny] = 0
            
sol(r-1,0,1)
print(res)