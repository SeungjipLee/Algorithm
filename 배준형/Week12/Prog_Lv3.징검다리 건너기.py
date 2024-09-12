def solution(stones, k):
    answer = 0
    n = len(stones)
    dp = [0] * n
    # 디딤돌이 0일때만 건너뛸 수 있음
    for idx, stone in enumerate(stones):
        print(dp)
        if idx < k:
            dp[idx] = stone
            for i in range(1, k+1):
                if idx-i < 0:
                    continue
                if stone > dp[idx-i]:
                    stone -= dp[idx-i]
                    dp[idx-i] = 0
                    continue
                else:
                    dp[idx-i] -= stone
                    break
        else:
            for i in range(1, k+1):
                if stone > dp[idx-i]:
                    stone -= dp[idx-i]
                    dp[idx] += dp[idx-i]
                    dp[idx-i] = 0
                    continue
                else:
                    dp[idx-i] -= stone
                    dp[idx] += stone
                    break
    print(dp)
    return sum(dp[-k:])