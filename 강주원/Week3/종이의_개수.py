import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minus_one = 0
zero = 0
one = 0

def sol(r, c, n):
    global minus_one, zero, one
    curr = arr[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != curr:
                nn = n // 3
                sol(r, c, nn)
                sol(r, c + nn, nn)
                sol(r, c + nn*2, nn)
                sol(r + nn, c, nn)
                sol(r + nn, c + nn, nn)
                sol(r + nn, c + nn*2, nn)
                sol(r + nn*2, c, nn)
                sol(r + nn*2, c + nn, nn)
                sol(r + nn*2, c + nn*2, nn)
                return
            
    if curr == -1:
        minus_one += 1
    elif not curr:
        zero += 1
    else:
        one += 1
    return

sol(0, 0, n)
print(minus_one)
print(zero)
print(one)