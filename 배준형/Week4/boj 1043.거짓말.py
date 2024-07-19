import sys
from collections import deque
def input_(): return sys.stdin.readline().rstrip()
def minput(): return map(int, input_().split())

N, M = minput()
graph = {i : [] for i in range(1, N+1)} # 누가 어느 파티에 갔는가
party = {i : [] for i in range(M)} # 몇 번 파티에는 누가 왔는지
visited_p = {i : False for i in range(1, N+1)}
parties = {i : False for i in range(M)}
T, *Ts = minput()


for i in range(M):
    num, *Ps = minput()
    party[i].extend(Ps)
    for p in Ps:
        graph[p].append(i)

for t in Ts:
    if visited_p[t]:
        continue
    q = deque()
    q.append(t)
    visited_p[t] = True
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if parties[nxt]:
                continue
            parties[nxt] = True
            for w in party[nxt]:
                if visited_p[w]:
                    continue
                q.append(w)
                visited_p[w] = True

answer = 0
for party in parties:
    if parties[party]:
        continue
    answer += 1
    
print(answer)
