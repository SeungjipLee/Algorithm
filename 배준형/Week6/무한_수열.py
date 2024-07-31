# A(0) = 1
# A(i) = A(⌊i/P⌋) + A(⌊i/Q⌋)
#  ⌊x⌋는 x를 넘지 않는 가장 큰 정수이다.

# A(N) 은?

# 메모리초과
import sys, math
def minput(): return map(int, sys.stdin.readline().split())

N, P, Q = minput()

dp = {}
dp[0] = 1
dp[1] = 2

if N != 0:
    p_ = int(math.log(N, P)) + 1
    q_ = int(math.log(N, Q)) + 1

    idxs = []
    for i in range(p_+1):
        for j in range(q_+1):
            if (N // (P**i*Q**j)) < 2:
                break
            idxs.append(N//(P**i*Q**j))

    idxs = list(set(idxs))
    idxs.sort()
    # print(idxs)

    for idx in idxs:
        dp[idx] = dp[idx//P] + dp[idx//Q]
# print(dp)

print(dp[N])

