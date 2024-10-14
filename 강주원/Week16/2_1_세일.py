n = int(input())
ls = [0] + sorted([int(input()) for _ in range(n)], reverse=True)

res = 0
for i in range(1, n+1):
    if i % 3 == 0:
        continue

    res += ls[i]

print(res)