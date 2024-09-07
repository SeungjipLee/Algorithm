import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]


def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in [(1,0), (0,1), (-1,0), (0,-1)]:
        nx = x + i[0]
        ny = y + i[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] >= arr[x][y]:
            continue

        cnt += dfs(nx, ny) 
    
    dp[x][y] = cnt
    return dp[x][y]


res = dfs(0, 0)
print(res)

