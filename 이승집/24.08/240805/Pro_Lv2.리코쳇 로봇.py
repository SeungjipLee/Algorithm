from pprint import pprint

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

n = len(board)
m = len(board[0])
board_cnt = [[-1]*m for _ in range(n)]


"""
-1 : 빈 공간
0 : 시작 점
-2 : 벽
"""
start_n = start_m = 0
goal_n = goal_m = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == "D":
            board_cnt[i][j] = -2
        elif board[i][j] == "R":
            board_cnt[i][j] = 1
            start_n, start_m = i, j
        elif board[i][j] == "G":
            board_cnt[i][j] = -3
            goal_n, goal_m = i, j

pprint(board_cnt)
print(start_n, start_m)
print(goal_n, goal_m)

