import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cats = sorted(list(map(int, input().split())))

i, j = 0, n-1
res = 0
while i < j:
    if cats[j] + cats[i] <= k:
        res += 1
        i += 1
    j -= 1

print(res)