def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2 or n == 3:
        return max(sticker)
    elif n == 4:
        return max(sticker[0]+sticker[2],sticker[1]+sticker[3])
    dp = [[0, 0] for _ in range(n)]
    # dp[x][0] = 0번 스티커 안뜯음
    # dp[x][1] = 0번 스티커 뜯음
    dp[0][1] = sticker[0]
    dp[1][0] = sticker[1]
    dp[1][1] = sticker[0]
    dp[2][0] = max(sticker[2], dp[1][0])
    dp[2][1] = dp[0][1] + sticker[2]
    dp[3][0] = max(dp[2][0], dp[1][0]+sticker[3])
    dp[3][1] = max(dp[2][1], dp[1][1]+sticker[3])
    for i in range(4, n):
        dp[i][0] = max(dp[i-1][0], dp[i-2][0]+sticker[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][1]+sticker[i])
    dp[n-1][1] = max(dp[n-2][1], dp[n-3][1])
    
    return max(dp[n-1])