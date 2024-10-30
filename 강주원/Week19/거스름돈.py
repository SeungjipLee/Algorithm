n = int(input())
res = 0
s = 1000 - n
for i in [500, 100, 50, 10, 5, 1]:
    res += s // i
    s %= i

print(res)