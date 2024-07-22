import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))
check = [0] * (n+1)

res = 0
for i in range(n):
    if check[i]:
        res += 1
        continue

    target = ls[i]
    first, second = 0, n-1
    while first < second:
        Sum = ls[first] + ls[second]
        if first == i:
            first += 1
            continue
        if second == i:
            second -= 1 
            continue
        
        if Sum < target:
            first += 1
        elif Sum > target:
            second -= 1
        else:
            res += 1
            check[i] = 1
            break

print(res)
