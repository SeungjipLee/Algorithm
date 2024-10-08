import sys
input = sys.stdin.readline

n, k = map(int, input().split())
caffeines = list(map(int, input().split()))

dp = [101] * 100001
dp[0] = 0

l = 0
for caffeine in caffeines:
    for j in range(l + caffeine, caffeine - 1, -1):
        dp[j] = min(dp[j], dp[j - caffeine] + 1)
    l += caffeine

if dp[k] == 101:
    print(-1)
else:
    print(dp[k])
