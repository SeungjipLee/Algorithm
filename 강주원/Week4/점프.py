import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
v[0][0] = 1

def sol():
    for i in range(n):
        for j in range(n):
            jump = board[i][j]
            if not jump or not v[i][j]:
                continue
            if i+jump < n:
                v[i+jump][j] += v[i][j]
            if j+jump < n:
                v[i][j+jump] += v[i][j]

    return v[-1][-1]

print(sol())