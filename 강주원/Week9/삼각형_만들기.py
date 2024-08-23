import sys
input = sys.stdin.readline

n = int(input())
ls = sorted([int(input()) for _ in range(n)], reverse=True)

res = -1
for i in range(n-2):
    if ls[i+1] + ls[i+2] > ls[i]:
        res = sum(ls[i:i+3])
        break

print(res)