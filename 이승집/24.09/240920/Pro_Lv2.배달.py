import heapq

N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
answer = 0

Adj = [[] for _ in range(N + 1)]

for a, b, c in road:
    Adj[a].append((b, c))
    Adj[b].append((a, c))

distance = [float('inf')] * (N + 1)
distance[1] = 0

heap = [(0, 1)]  # (누적 시간, 현재 노드)

while heap:
    current_time, now = heapq.heappop(heap)

    if current_time > distance[now]:
        continue

    for neighbor, cost in Adj[now]:
        time = current_time + cost
        if time <= K and time < distance[neighbor]:
            distance[neighbor] = time
            heapq.heappush(heap, (time, neighbor))

print(distance)
answer = sum(1 for d in distance if d <= K)

print(answer)
