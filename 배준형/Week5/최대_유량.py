# 직선 처리
# 병렬 처리
# 직선 처리
# 반복해서 하다가
# 하나 남으면 합치기 

# 양 방향으로 흐름..

import sys
from collections import deque
input_ = sys.stdin.readline

N = int(input_())
adj_dict ={}

for _ in range(N):
    a, b, size = input_().rstrip().split()
    size = int(size)
    
    if adj_dict.get(a):
        if adj_dict[a].get(b):
            adj_dict[a][b] += size
        else:
            adj_dict[a][b] = size
    else:
        adj_dict[a] = {}
        adj_dict[a][b] = size
        
    if adj_dict.get(b):
        if adj_dict[b].get(a) == None:
            adj_dict[b][a] = 0
    else:
        adj_dict[b] = {}
        adj_dict[b][a] = 0


def dfs():
    amount_flow = 0
    
    # while True:
    for _ in range(1):
        q = deque()
        path = {u : "" for u in adj_dict}
        visited = {u : False for u in adj_dict}
        q.append("A")
        visited["A"] =  True
        path["A"] = "A"
        
        while q:
            now = q.popleft()
            for nxt in adj_dict[now]:
                print(adj_dict)
                if visited[nxt]:
                    continue
                if adj_dict[now][nxt] <= 0:
                    continue
                print(now, nxt)
                q.append(nxt)
                path[nxt] = now
                visited[nxt] = True
        
        if not visited["Z"]:
            break
        
        cur = "Z"
        min_C = int(10e9)
        while cur != "A":
            pre = path[cur]
            min_C = min(min_C, adj_dict[pre][cur])
            cur = pre
            
        cur = "Z"
        while cur != "A":
            pre = path[cur]
            adj_dict[pre][cur] -= min_C
            adj_dict[cur][pre] += min_C
            cur = pre
            
        amount_flow += min_C
    return amount_flow           
    
print(dfs())
# print(adj_dict)