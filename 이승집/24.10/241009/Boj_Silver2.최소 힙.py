import heapq
import sys

input = sys.stdin.readline

N = int(input())

arr = []
output = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if arr:
            output.append(str(heapq.heappop(arr)))
        else:
            output.append('0')
    else:
        heapq.heappush(arr, a)

print('\n'.join(output))
