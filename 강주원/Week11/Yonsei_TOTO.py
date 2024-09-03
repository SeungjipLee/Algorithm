import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mileage_lst = []
for i in range(n):
    p, l = map(int, input().split())
    ls = sorted(list(map(int, input().split())), reverse=True)
    if len(ls) >= l:
        min_mileage = ls[l-1]
    else:
        min_mileage = 1
    mileage_lst.append(min_mileage)

mileage_lst.sort()
res = 0
for mileage in mileage_lst:
    if m >= mileage:
        m -= mileage
        res += 1

print(res)