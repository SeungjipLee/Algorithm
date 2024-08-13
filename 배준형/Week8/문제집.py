# N개의 문제는 모두 풀어야 한다.
# 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 가능하면 쉬운 문제부터 풀어야 한다.

# 첫째 줄에 문제의 수 N(1 ≤ N ≤ 32,000)과 먼저 푸는 것이 좋은 문제에 대한 정보의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다. 이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.

# 1 2 3 4
# 1 번보다 4번을 먼저 풀면 좋음
# 2 번보다 3번을 먼저 풀면 좋음
# 4 -> 1, 3 -> 2
# 3 2 4 1
import sys
import heapq
from collections import deque
def minput(): return map(int, sys.stdin.readline().split())

N, M = minput()

h = []
adj_ls = [[] for _ in range(N+1)]
visited = [False] * (N+1)
orders = [0] * (N+1)

def bfs(num):
    seq = deque()
    tmp_h = []
    heapq.heappush(tmp_h, num)
    visited[num] = True
    
    while tmp_h:
        now = heapq.heappop(tmp_h)
        seq.append(now)
        
        for nxt in adj_ls[now]:
            orders[nxt] -= 1
            if orders[nxt] == 0:
                heapq.heappush(tmp_h, nxt)
                visited[nxt] = True
    return seq

# 진입차수 정해야 함
for _ in range(M):
    # a 를 b 보다 먼저 풀어라
    a, b = minput()
    adj_ls[a].append(b)
    orders[b] += 1

q = deque()
for i in range(1, N+1):
    if orders[i] == 0:
        q.append(i)
# print(q)
while q:
    prob = q.popleft()
    heapq.heappush(h, bfs(prob))
# print(h)
while h:
    now = heapq.heappop(h)
    print(now.popleft(), end=" ")
    if now:
        heapq.heappush(h, now)



# def bfs(num):
#     seq = deque()
#     seq.append(num)
#     tmp_q = deque()
#     tmp_q.append([num, 0])
#     visited[num] = True
#     tmp = []
#     pre = 0
    
#     while tmp_q:
#         now, cnt = tmp_q.popleft()
        
#         if cnt != pre:
#             seq.extend(sorted(tmp))
#             tmp = []
#             pre += 1
            
#         for nxt in sorted(adj_ls[now]):
#             if visited[nxt]:
#                 continue
#             orders[nxt] -= 1
#             if orders[nxt] == 0:
#                 visited[nxt] = True
#                 tmp_q.append([nxt, cnt+1])
#                 tmp.append(nxt)    
#     return seq