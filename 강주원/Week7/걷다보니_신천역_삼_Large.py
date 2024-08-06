n = int(input())
dp = [0] * 33334
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] * 3) % 1000000009

print(dp[n])