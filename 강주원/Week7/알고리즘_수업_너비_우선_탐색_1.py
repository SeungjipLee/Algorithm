import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for i in sorted(graph[x]):
            if not visit[i]:
                cnt += 1
                visit[i] = cnt
                q.append(i)                

bfs(r)
for i in visit[1:]:
    print(i)