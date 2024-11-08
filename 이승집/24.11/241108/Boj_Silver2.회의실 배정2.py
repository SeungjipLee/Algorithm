n = int(input())

arr = []
dp = [0] * n
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[1])
print(arr)

dp[0] = arr[0][2]
for i in range(1, n):
    now = arr[i][2]
    for j in range(i - 1, -1, -1):
        if arr[i][0] >= arr[j][1]:
            now += dp[j]
            break

    dp[i] = max(dp[i - 1], now)

print(dp)
