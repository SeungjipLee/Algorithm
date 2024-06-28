import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [0] * (k+1)

for coin in coins:
    if coin > k:
        break
    dp[coin] = 1
    for i in range(k+1):
        if i - coin >= 0 and dp[i-coin]:
            if dp[i] == 0:
                dp[i] = dp[i-coin] + 1
            else:
                dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k]:
    print(dp[k])
else:
    print(-1)