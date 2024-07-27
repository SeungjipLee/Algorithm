import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
visit = [0] * n
res = []

def sol(start):
    if len(res) == m:
        print(*res)
        return
    temp = 0
    for i in range(start, n):
        if not visit[i] and temp != ls[i]:
            res.append(ls[i])
            temp = ls[i]
            visit[i] = 1
            sol(i)
            visit[i] = 0
            res.pop()

sol(0)

