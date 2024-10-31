def solution(land):
    answer = 0

    n, m = len(land), len(land[0])
    memo = [[0] * m for _ in range(n)]
    for i in range(m):
        memo[0][i] = land[0][i]
        
    for i in range(n-1):
        for j in range(m):
            for k in range(m):
                if j == k:
                    continue
                memo[i+1][k] = max(memo[i+1][k], memo[i][j] + land[i+1][k])
    # print(memo)    
    return max(memo[-1])