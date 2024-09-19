import sys
input = sys.stdin.readline

dp = [1] * 68
dp[2], dp[3] = 2, 4
for i in range(4, 68):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

t = int(input())
for _ in range(t):
    print(dp[int(input())])