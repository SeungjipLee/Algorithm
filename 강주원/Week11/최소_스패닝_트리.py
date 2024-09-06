import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]


def find_parent(x):
    if x == parent[x]:
        return x
    
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    parent[max(a,b)] = min(a,b)


res = 0
for a, b, cost in edges:
    if find_parent(a) != find_parent(b):
       res += cost
       union_parent(a,b) 

print(res)