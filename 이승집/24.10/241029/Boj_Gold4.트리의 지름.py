import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
Adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    Adj[a].append((b, c))
    Adj[b].append((a, c))


def bfs(start):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        curr = queue.popleft()
        for neighbor, weight in Adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[curr] + weight
                queue.append(neighbor)
        print(distance)
        print(visited)
    max_distance = max(distance)
    farthest_node = distance.index(max_distance)
    return farthest_node, max_distance


node_far, _ = bfs(1)
_, diameter = bfs(node_far)
print(diameter)
