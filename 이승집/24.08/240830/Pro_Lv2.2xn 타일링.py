n = 4

memo = [0] * (n + 1)
memo[1] = 1
memo[2] = 2
k = 3
while k <= n:
    memo[k] = (memo[k-2] + memo[k-1])%1000000007
    k += 1

print(memo[n])