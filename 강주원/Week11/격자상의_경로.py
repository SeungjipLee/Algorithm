import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
ki, kj = n-1, m-1
for i in range(n):
    for j in range(m):
        val = i*m+j+1
        arr[i][j] = val
        if val == k:
            ki, kj = i, j

dp = [[0]*m for _ in range(n)]

dp[0][0] = 1
for i in range(ki+1):
    for j in range(kj+1):
        if i == 0 and j == 0:
            continue

        r = dp[i-1][j]
        c = dp[i][j-1]
        dp[i][j] = r + c


for i in range(ki,n):
    for j in range(kj,m):
        if i == ki and j == kj:
            continue

        r = dp[i-1][j]
        c = dp[i][j-1]
        dp[i][j] = r + c


print(dp[n-1][m-1])