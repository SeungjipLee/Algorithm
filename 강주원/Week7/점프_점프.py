from collections import deque
n = int(input())
ls = list(map(int, input().split()))
visit = [0] * 100000

res = 1e9
def bfs(x):
    global res
    q = deque()
    q.append([x,0])
    visit[x] = 1
    while q:
        x, cnt = q.popleft()
        if x >= n-1:
            res = min(res, cnt)
            continue
        
        for i in range(1, ls[x]+1):
            next = x + i
            if next >= n or visit[next] and visit[next] <= cnt + 1:
                continue
            visit[next] = cnt + 1
            q.append([next, cnt+1])

bfs(0)
if res == 1e9:
    res = -1
print(res)