import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, n+1):
    arr[i].sort()

visit = [0] * (n+1)

res = []
cnt = 1
def dfs(start):
    global cnt
    visit[start] = cnt
    for i in arr[start]:
        if not visit[i]:
            cnt += 1
            dfs(i)

dfs(r)
# for i in range(1, n+1):
#     print(visit[i])
print(visit)