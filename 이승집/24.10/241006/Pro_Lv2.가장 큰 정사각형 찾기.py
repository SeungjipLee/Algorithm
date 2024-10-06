def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:  # 첫 행이나 첫 열인 경우
                    dp[i][j] = 1
                else:
                    # 현재 위치의 값은 좌, 상, 좌상 값의 최소값 + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 최대 정사각형 한 변의 길이 갱신
                if dp[i][j] > max_side:
                    max_side = dp[i][j]

    # 최대 정사각형의 넓이 반환
    return max_side ** 2
