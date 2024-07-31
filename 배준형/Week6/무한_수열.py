# A(0) = 1
# A(i) = A(⌊i/P⌋) + A(⌊i/Q⌋)
#  ⌊x⌋는 x를 넘지 않는 가장 큰 정수이다.

# A(N) 은?
import sys
def minput(): return map(int, sys.stdin.readline().split())

N, P, Q = minput()

dp = {}
dp[0] = 1

for i in range(1, N//min(P, Q)+1):
    dp[i] = dp[i//P] + dp[i//Q]

if N == 0:
    print(1)
else:
    print(dp[N//P] + dp[N//Q])

