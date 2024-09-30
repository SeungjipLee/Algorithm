import sys
input = sys.stdin.readline

n = int(input())
dragon_curves = [list(map(int, input().split())) for _ in range(n)]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
arr = [[0] * 101 for _ in range(101)]

    
for y, x, d, g in dragon_curves:
    arr[x][y] = 1
    
    ls = [d]
    for j in range(g):
        for k in range(len(ls)-1, -1, -1):
            ls.append((ls[k] + 1) % 4)

    for j in range(len(ls)):
        x += dx[ls[j]]
        y += dy[ls[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue

        arr[x][y] = 1

res = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            res += 1

print(res)