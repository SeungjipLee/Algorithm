import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))
res = 0

if n % 2 == 1:
    res = ls.pop()

for i in range(n//2):
    res = max(res, ls[i] + ls[-i-1])

print(res)