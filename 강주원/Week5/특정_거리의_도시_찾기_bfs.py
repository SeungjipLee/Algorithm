import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
visit = [0] * (n+1)
dist = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    # 단방향
    arr[a].append(b)

res = []
def bfs(v):
    visit[v] = 1
    q = deque([v])
    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visit[i]:
                visit[i] = 1
                q.append(i)
                # 이전 거리 + 1
                dist[i] = dist[now] + 1
                if dist[i] == k:
                    res.append(i)

bfs(x)
if res:
    res.sort()
    for i in res:
        print(i)
else:
    print(-1)