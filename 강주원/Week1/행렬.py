import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mat_a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
mat_b = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def check(i,j):
    for a in range(i, i+3):
        for b in range(j, j+3):
            mat_a[a][b] = 1 if not mat_a[a][b] else 0

res = 0
if n < 3 or m < 3:
    if mat_a != mat_b:
        res = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if mat_a[i][j] != mat_b[i][j]:
                res += 1
                check(i, j)

print(res)