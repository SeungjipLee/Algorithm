# 창렬을 좋아하는 민규
n = int(input())
ls = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], ls[j] + dp[i-j])

print(dp[n])