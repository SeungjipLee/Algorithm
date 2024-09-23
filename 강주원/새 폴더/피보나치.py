import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
fibo = [0, 1]
for i in range(2, 46):
    fibo.append(fibo[i-2] + fibo[i-1])


def binary(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if fibo[mid] == target:
            return mid
        
        if fibo[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return end
    

for tc in range(t):
    n = int(input())
    res = []

    start, end = 1, 45
    while n > 0:
        idx = binary(start, end, n)
        n -= fibo[idx]
        end = idx - 1
        res.appendleft(fibo[idx])
    
    print(*res)


