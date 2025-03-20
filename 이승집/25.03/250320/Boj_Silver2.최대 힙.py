import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
H = []
for _ in range(n):
    v = int(input())
    if v > 0:
        heappush(H, -v)
    else:
        if H:
            print(-heappop(H))
        else:
            print(0)