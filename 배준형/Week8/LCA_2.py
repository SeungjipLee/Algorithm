import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

def find_parents(a, b, parents, rank):
    rank_a = rank[a]
    rank_b = rank[b]
    
    while True:
        if rank_a != rank_b:
            if rank_a > rank_b:
                rank_a -= 1
                a = parents[a]
            else:
                rank_b -= 1
                b = parents[b]
        elif rank_a == rank_b:
            if a == b:
                return a
            else:
                rank_a -= 1
                rank_b -= 1
                a = parents[a]
                b = parents[b]

N = int(input_())
parents = [0] * (N+1)
parents[1] = 1
rank = [0] * (N+1)
rank[1] = 1
adj_ls = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = minput()
    adj_ls[a].append(b)
    adj_ls[b].append(a)

q = deque()
visited = [0] * (N+1)
q.append(1)

while q:
    p = q.popleft()
    visited[p] = 1

    for c in adj_ls[p]:
        if visited[c]:
            continue
        # 트리의 몇층인지
        rank[c] = rank[p] + 1
        parents[c] = p

        q.append(c)
    
M = int(input_())
for _ in range(M):
    a, b = minput()
    print(find_parents(a, b, parents, rank))