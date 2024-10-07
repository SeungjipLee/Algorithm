import sys
input = sys.stdin.readline

n, k = map(int, input().split())
caffeines = sorted(list(map(int, input().split())))
'''
5
0 1 1 2 3 5
한계가 1이면?
카페인 1 하나 택
2이면
1 두개 혹은 2 하나 택
3이면
3 하나 택 혹은 2 하나 1하나 택
4이면 
'''
ls = [[0, 0]]
for i in range(1, n+1):
    caffeine = caffeines[i-1]
    ls.append([caffeine, caffeine])
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(k+1):
    dp[0][i] = 1e9
    
for i in range(1, n+1):
    for j in range(1, k+1):
        if j - caffeines[i-1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-caffeines[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]

res = dp[n][k]
if res == 1e9:
    res = -1

print(res)
