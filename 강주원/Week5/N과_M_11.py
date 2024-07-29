import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
temp = []

def sol():
    if len(temp) == m:
        print(*temp)
        return
    
    now = 0
    for i in range(n):
        if now != ls[i]:
            now = ls[i]
            temp.append(now)
            sol()
            temp.pop()

sol()
