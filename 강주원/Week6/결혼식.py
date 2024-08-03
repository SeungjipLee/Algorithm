import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [0] * (n+1)
res = 0
for friend in arr[1]:
    if not visit[friend]:
        visit[friend] = 1
        res += 1

    for ffriend in arr[friend]:
        if not visit[ffriend] and ffriend != 1:
            visit[ffriend] = 1
            res += 1

print(res)