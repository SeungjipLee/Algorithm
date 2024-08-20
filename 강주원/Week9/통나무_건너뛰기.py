import sys, heapq
from collections import deque
input = sys.stdin.readline

t = int(input())

def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    ls = []
    idx = 0
    while arr:
        ls.insert(idx, heapq.heappop(arr))
        idx += 1
        if arr:
            ls.insert(-idx, heapq.heappop(arr))
        

    res = 0
    for i in range(n):
        diff = abs(ls[i] - ls[i-1])
        res = max(res, diff)

    return res

for tc in range(t):
    print(sol())

'''
10 11 12 13 12 11 10
'''