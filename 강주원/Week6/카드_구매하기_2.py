n = int(input())
ls = [1e9] + list(map(int, input().split()))
dp = [0] + [1e9] * n

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], ls[j] + dp[i-j])
print(dp[n])