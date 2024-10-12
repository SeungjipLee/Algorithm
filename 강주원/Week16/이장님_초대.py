import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())), reverse=True)

res = 0
for i in range(n):
    res = max(res, (i+1)+1+ls[i])

print(res)