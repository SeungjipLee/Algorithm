n = int(input())
dp = [1] * (n+1)

# dp[1] = 1 + 2 # 2 + 1
# dp[2] = 1 + 4 + 2 # 6 + 1
# dp[3] = 1 + 6 + 8 + 2 # 16 + 1
# dp[4] = 1 + 8 + 18 + 12 + 2 # 40 + 1
dp[1] = 3
# dp[2] = 7


for i in range(2,n+1):
    dp[i] = dp[i-1] * 2 + dp[i-2]

print(dp[n]%9901)