import heapq
n, k, a, b = map(int, input().split())

flowerpots = [k] * n
heapq.heapify(flowerpots)

day = 0
while 0 not in flowerpots:
    for i in range(a):
        moisture = heapq.heappop(flowerpots)
        heapq.heappush(flowerpots, moisture + b)
    
    for i in range(n):
        flowerpots[i] -= 1
    
    day += 1

print(day)
