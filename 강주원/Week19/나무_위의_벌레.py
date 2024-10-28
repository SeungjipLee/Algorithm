import sys
input = sys.stdin.readline

n = int(input())
fruits = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append([b, fruits[b]])
    graph[b].append([a, fruits[a]])


def dfs(v,c):
    for next_node, cost in graph[v]:
        if visited[next_node] == -1:
            visited[next_node] = c + cost
            dfs(next_node, c+cost)


# 1번 노드에서 가장 먼 곳을 찾는다.
visited = [-1] * (n+1)
visited[1] = fruits[1]
dfs(1, fruits[1])
max_val = max(visited)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
last_Node = []
for i, data in enumerate(visited[1:]):
    if data == max_val:
        last_Node.append(i+1)

res = [0, 1]
for node in last_Node:
    visited = [-1] * (n + 1)
    visited[node] = fruits[node]
    dfs(node, fruits[node])
    max_val = max(visited)
    for i, data in enumerate(visited[1:]):
        if data == max_val:
            res = [data, i+1]
            break


print(*res)