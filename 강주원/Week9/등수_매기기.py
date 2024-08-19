import sys
input = sys.stdin.readline

n = int(input())
ls = sorted([int(input()) for _ in range(n)])
res = 0
for i in range(n):
    res += abs(ls[i] - (i+1))

print(res)