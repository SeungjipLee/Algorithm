import sys
input = sys.stdin.readline

n = int(input())
ls = sorted([int(input()) for _ in range(n)], reverse=True)

res = 0
for i in range(n):
    tip = ls[i] - i
    if tip > 0:
        res += tip

print(res)