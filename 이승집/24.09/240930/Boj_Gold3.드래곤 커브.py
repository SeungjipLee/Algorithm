from copy import deepcopy

"""
input
3
3 3 0 1
4 2 1 3
4 2 2 1

di = 0 : 오른쪽 이므로 아래
    고정점 : (1, -1)
    회전점 : (0, 0), (1, 0)
di = 1 : 위쪽 이므로 오른쪽
di = 2 : 왼쪽 이므로 위로
di = 3 : 아래 이므로 왼쪽
"""

board = [[0] * 201 for _ in range(201)]


def cnt_board():
    cnt = 0
    for i in range(100, 200):
        for j in range(100, 200):
            if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
                cnt += 1
    return cnt


def rot(arr):
    fx, fy = arr.pop()
    mid = []
    while arr:
        rx, ry = arr.pop()
        rx -= fx
        ry -= fy
        nx = -ry + fx
        ny = rx + fy
        mid.append((nx, ny))
    return mid


dix = [1, 0, -1, 0]
diy = [0, -1, 0, 1]

N = int(input())

for _ in range(N):
    sx, sy, di, ge = map(int, input().split())
    stack = [(sx, sy), (sx+dix[di], sy+diy[di])]
    while ge > 0:
        s = deepcopy(stack)
        stack += rot(s)
        ge -= 1
    for px, py in stack:
        if 0 <= px <= 100 and 0 <= py <= 100:
            board[px + 100][py + 100] = 1

print(cnt_board())