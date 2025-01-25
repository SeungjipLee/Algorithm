import sys
input = sys.stdin.readline

N, K = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(N)]
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
horses = {i: [] for i in range(1, K + 1)}
board = [[[] for _ in range(N)] for _ in range(N)]
turn = 0

for i in range(K):
    r, c, d = map(int, input().split())
    horses[i + 1].append(r - 1)
    horses[i + 1].append(c - 1)
    horses[i + 1].append(d - 1)
    board[r - 1][c - 1].append(i + 1)
    

def changeDirection(d):
    if d == 0 or d == 2:
        return d + 1

    elif d == 1 or d == 3:
        return d - 1
    

def nextBlueOrOutofBoard(k, r, c, d):
    nd = changeDirection(d)
    horses[k][2] = nd
    nr, nc = r + move[nd][0], c + move[nd][1]
    
    if 0 <= nr < N and 0 <= nc < N:
        if colors[nr][nc] == 0:
            while board[r][c]:
                popped = board[r][c].pop(0)
                horses[popped][0], horses[popped][1] = nr, nc
                board[nr][nc].append(popped)

        
        elif colors[nr][nc] == 1:
            while board[r][c]:
                popped = board[r][c].pop()
                horses[popped][0], horses[popped][1] = nr, nc
                board[nr][nc].append(popped)
        


def moveHorses():
    for k in horses.keys():
        r, c, d = horses[k][0], horses[k][1], horses[k][2]
        first = board[r][c][0]
        if first == k:
            nr, nc = r + move[d][0], c + move[d][1]
            if (nr < 0 or nr >= N or nc < 0 or nc >= N) or colors[nr][nc] == 2:
                nextBlueOrOutofBoard(k, r, c, d)
            
            else:
                if colors[nr][nc] == 0:
                    while board[r][c]:
                        popped = board[r][c].pop(0)
                        horses[popped][0], horses[popped][1] = nr, nc
                        board[nr][nc].append(popped)
                
                elif colors[nr][nc] == 1:
                    while board[r][c]:
                        popped = board[r][c].pop()
                        horses[popped][0], horses[popped][1] = nr, nc
                        board[nr][nc].append(popped)
                
              
while True:
    moveHorses()
    turn += 1

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) >= 4:
                print(turn)
                exit()

    if turn > 1000:
        print(-1)
        exit()