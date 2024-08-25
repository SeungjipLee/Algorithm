import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = []

for i in range(n):
    a, b = input().split()
    b = int(b)
    ls.append([a,b])

def binary(target):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if ls[mid][1] >= target:
            index = mid
            r = mid - 1
        else:
            l = mid + 1

    return index    

for i in range(m):
    print(ls[binary(int(input()))][0])