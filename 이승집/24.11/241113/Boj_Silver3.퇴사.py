n = int(input())
t = []
p = []
for _ in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + t[i] <= n:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
