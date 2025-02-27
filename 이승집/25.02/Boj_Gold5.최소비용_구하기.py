import sys
import heapq

def main():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    adj = {i:[] for i in range(1, n + 1)}
    for _ in range(m):
        s, e, cost = map(int, input().split())
        adj[s].append((e, cost))
    start, end = map(int, input().split())


    def dijkstra(adj, start, n):
        INF = float('inf')
        distance = [INF] * (n + 1)
        distance[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            cost, node = heapq.heappop(pq)

            if distance[node] < cost:
                continue

            for neighbor, weight in adj.get(node, []):
                new_cost = cost + weight
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))

        return distance

    min_cost = dijkstra(adj, start, n)
    print(min_cost[end])


if __name__ == "__main__":
    main()

"""input
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""