import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    # 단방향
    arr[a].append([b, 1])

res = []

def dijkstra(v):
    hq = []
    heapq.heappush(hq, [0, v])
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq, [cost, i[0]])

dijkstra(x)
for i in range(1, n+1):
    if distance[i] == k:
        res.append(i)

if res:
    res.sort()
    for i in res:
        print(i)
else:
    print(-1)