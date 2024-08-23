import sys
import heapq
def minput(): return map(int, sys.stdin.readline().split())

K, N = minput()
arr = list(minput())
h = []
for i in range(K):
    heapq.heappush(h, [arr[i], i])

cnt = 0
now = -1
max_val = max(arr)
while cnt != N:
    cnt += 1
    
    now, idx = heapq.heappop(h)
    for j in range(idx, K):
        if now*arr[j] > 2**31:
            break
        
        if len(h) > N and now*arr[j] > max_val:
            break
        max_val = max(max_val, now*arr[j])
        heapq.heappush(h, [now*arr[j], j])

print(now)