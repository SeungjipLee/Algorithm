board = [list(map(int, input().split())) for _ in range(5)]
res = set()

def dfs(x,y,s):
    if len(s) == 6:
        res.add(s)
        return
    
    for i in [(1,0), (0,1), (-1,0), (0,-1)]:
        nx = x + i[0]
        ny = y + i[1]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        ns = s + str(board[nx][ny])
        dfs(nx,ny,ns)

for i in range(5):
    for j in range(5):
        dfs(i,j,str(board[i][j]))

print(len(res))