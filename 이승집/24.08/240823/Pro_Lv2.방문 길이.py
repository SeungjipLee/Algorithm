Board = [[[0]*4 for _ in range(11)] for _ in range(11)]
dirs = "LULLLLLLU"
answer = 0
now_x, now_y = 5, 5

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_idx = {"R": 0, "D": 1, "L": 2, "U": 3}

for i in dirs:
    next_x, next_y = now_x + dx[dir_idx[i]], now_y + dy[dir_idx[i]]
    if next_x < 0 or next_x > 10 or next_y < 0 or next_y > 10:
        continue
    if Board[now_x][now_y][dir_idx[i]] == 0:
        Board[now_x][now_y][dir_idx[i]] = 1
        Board[next_x][next_y][(dir_idx[i] + 2) % 4] = 1
        answer += 1
    now_x, now_y = next_x, next_y

print(answer)