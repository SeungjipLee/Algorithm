board = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]

n = len(board[0])
h = 0
w = 1
answer = 0

# 기준 색 저장
standard = board[h][w]

# 아래
if (0 <= h + 1 < n) and board[h+1][w] == standard:
    answer += 1

# 위
if (0 <= h - 1 < n) and board[h - 1][w] == standard:
    answer += 1

# 오른쪽
if (0 <= w + 1 < n) and board[h][w + 1] == standard:
    answer += 1

# 왼쪽
if (0 <= w - 1 < n) and board[h][w - 1] == standard:
    answer += 1

print(answer)