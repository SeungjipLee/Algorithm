import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
S = [0] + list(map(int, input().split()))
edges = []
parent = [i for i in range(n+1)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        if S[a] < S[b]:
            parent[b] = a
        else:
            parent[a] = b

ls = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    union_parent(a, b)

components = set(parent[1:])
components_min_costs = {}
for i in range(1, n+1):
    root = find_parent(i)
    if root not in components_min_costs:
        components_min_costs[root] = S[i]
    else:
        components_min_costs[root] = min(components_min_costs[root], S[i])

min_costs = list(components_min_costs.values())
min_costs.sort()


total = 0
for i in range(1, len(min_costs)):
    total += min_costs[0] * min_costs[i]

print(total)