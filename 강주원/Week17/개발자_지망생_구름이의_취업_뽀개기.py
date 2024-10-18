import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
res = 240
for i in p[1:]:
    if not i:
        res -= 60
a = [[] for _ in range(6)]
for i in range(n):
    k, t = map(int, input().split())
    a[k].append(t)

for i in range(1, 6):
    a[i].sort()


for i in range(1, 6):
    res += a[i][0]
    for j in range(1, p[i]):
        res += a[i][j] + (a[i][j] - a[i][j-1])

print(res)