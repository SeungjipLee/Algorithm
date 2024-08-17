import sys
input = sys.stdin.readline

t = int(input())

def sol():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    i, j, unit, res = 0, 0, 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            i += 1
            res += unit
        else:
            unit += 1
            j += 1
    if j >= m:
        res += len(a[i:])*unit
    
    return res

for tc in range(t):
    print(sol())