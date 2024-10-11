import heapq
n = int(input())
ls = list(map(int, input().split()))
hq = []
for i in ls:
    heapq.heappush(hq, -i)

res = 0
while hq:
    first = -heapq.heappop(hq)
    if hq:
        second = -heapq.heappop(hq)
        res += second
        heapq.heappush(hq, -(first-second))
    else:
        res += first
        break

if res <= 1440:
    print(res)
else:
    print(-1)