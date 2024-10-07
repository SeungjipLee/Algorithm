N, K = map(int, input().split())
caffeine = list(map(int, input().split()))

dp = [int(1e9)] * (K + 1)
dp[0] = 0

for c in caffeine:
    for i in range(K, c - 1, -1):
        if dp[i - c] + 1 < dp[i]:
            dp[i] = dp[i - c] + 1

if dp[K] == int(1e9):
    print(-1)
else:
    print(dp[K])