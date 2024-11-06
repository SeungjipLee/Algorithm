n = int(input())
b = list(map(int, input().split()))

f = b[0]
res = 0
cnt = 0
for i in range(1, n):
    if b[i] > f:
        f = b[i]
        res = max(res, cnt)
        cnt = 0
    else:
        cnt += 1

print(max(res, cnt))