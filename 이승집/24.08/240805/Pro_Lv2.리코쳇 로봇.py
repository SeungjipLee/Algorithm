from collections import deque

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

n = len(board)
m = len(board[0])
answer = 0

# 4방향(좌 우 상 하)
dn, dm = [0, 0, -1, 1], [-1, 1, 0, 0]
start = [-1, -1]
visit = [[False] * m for _ in range(n)]


def move(i, j, dir):
    global n, m

    while True:
        i += dn[dir]
        j += dm[dir]
        if i < 0 or i >= n or j < 0 or j >= m:
            i -= dn[dir]
            j -= dm[dir]
            break
        elif board[i][j] == 'D':
            i -= dn[dir]
            j -= dm[dir]
            break
    return [i, j]


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            start = [i, j]
            break
    if start[0] != -1:
        break

Q = deque()
Q.appendleft([start[0], start[1], 0])
visit[start[0]][start[1]] = True

while Q:
    i, j, dis = Q.pop()
    for k in range(4):
        N, M = move(i, j, k)

        if visit[N][M]:
            continue
        elif board[N][M] == 'G':
            answer = dis + 1
            Q = []
            break
        else:
            visit[N][M] = True
            Q.appendleft([N, M, dis + 1])

if answer == 0:
    answer = -1

print(answer)