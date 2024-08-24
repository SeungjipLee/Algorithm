import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
# 트리 위에는 1개의 말이 있는데,
# 각 플레이어는 자신의 턴에 간선으로 이어진 인접한 정점으로 말을 옮겨야 합니다. 
# 단, 한 번 방문했던 정점으로는 이동할 수 없으며, 더는 말을 움직일 수 없게 되면 게임이 종료됩니다. 
# 이때 게임 진행 과정에서 
# 한 번이라도 말이 목표 정점 E를 방문했다면 선공의 승리이고, 
# 그렇지 못하면 후공의 승리입니다.

# 목표 노드로가는 분기점 마다 자신이 선택할 수 있으면 선공
N, S, E = minput()
adj_ls = [[] for i in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = minput()
    adj_ls[a].append(b)
    adj_ls[b].append(a)

q = deque()
visited = [False] * (N+1)
visited[S] = True
q.append(S)
while q:
    now = q.popleft()
    for nxt in adj_ls[now]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        parents[nxt] = now
        q.append(nxt)

child = [0] * (N+1)
i = E
while parents[i] != i:
    child[parents[i]] = i
    i = parents[i]

i = S
visited = [False] * (N+1)
visited[i] = True
while True:
    
    i = child[i]
    visited[i] = True
    junction = False
    if i == E:
        break

    for j in adj_ls[i]:
        if visited[j]:
            continue
        if j != child[i]:
            junction = True

    if junction:
        print('Second')
        exit()
    i = child[i]
    visited[i] = True
    if i == E:
        break
print('First')