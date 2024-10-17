import sys

input = sys.stdin.readline

"""
계단을 선택함에 있어 연속된 3개를 선택할 수 없으므로

전과 그 전까지도 고려를 해야한다.
"""


N = int(input())
stairs = [0] * (N + 1)

for i in range(1, N + 1):
    stairs[i] = int(input())

print(stairs)

if N == 1:
    print(stairs[1])
else:
    dp = [0] * (N + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[N])
