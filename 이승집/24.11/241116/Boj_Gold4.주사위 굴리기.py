dice = [0, 0, 0, 0, 0, 0]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
do = list(map(int, input().split()))

def go(n):
    global dice
    if n == 1:
        dice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    elif n == 2:
        dice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    elif n == 3:
        dice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    elif n == 4:
        dice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in do:
    nx, ny = x + dx[i - 1], y + dy[i - 1]
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    go(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])
    x, y = nx, ny
