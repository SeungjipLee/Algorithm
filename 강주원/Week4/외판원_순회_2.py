import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [0]*n
res = 1e9

def back(start, v, cost, depth):
    global res
    if depth == n:
        if arr[v][start]:
            res = min(res, cost+arr[v][start])
        return
    
    if cost > res:
        return

    for i in range(n):
        if not visit[i] and arr[v][i]:
            visit[i] = 1
            back(start, i, cost + arr[v][i], depth+1)
            visit[i] = 0

for i in range(n):
    visit[i] = 1
    back(i, i, 0, 1)
    visit[i] = 0

print(res)