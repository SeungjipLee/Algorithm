from collections import deque

dx = [0, 1]
dy = [1, 0]
ex = [-1, 0]
ey = [0, -1]


def solution(m, n, puddles):
    answer = 0
    board = [[0] * m for _ in range(n)]
    for puddle in puddles:
        board[puddle[1] - 1][puddle[0] - 1] = -1

    Q = deque([(0, 0)])
    board[0][0] = 1

    while Q:
        now_x, now_y = Q.popleft()
        mid = [0, 0]
        for l in range(2):
            prev_x = now_x + ex[l]
            prev_y = now_y + ey[l]
            if prev_x < 0 or prev_x >= n or prev_y < 0 or prev_y >= m or board[prev_x][prev_y] == -1:
                continue
            mid[l] = board[prev_x][prev_y]

        if now_x == now_y == 0:
            pass
        else:
            board[now_x][now_y] = sum(mid)

        for k in range(2):
            next_x = now_x + dx[k]
            next_y = now_y + dy[k]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            if board[next_x][next_y] != 0:
                continue
            Q.append((next_x, next_y))

    print(board)

    return answer

solution(4, 3, [[2, 2]])


"""
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    
    for x in range(n):
        for y in range(m):
            if dp[x][y] == -1:
                dp[x][y] = 0
                continue
            
            if x > 0:
                dp[x][y] += dp[x-1][y]
            
            if y > 0:
                dp[x][y] += dp[x][y-1]
            
            dp[x][y] %= 1_000_000_007
    
    return dp[n-1][m-1]
"""

