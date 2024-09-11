import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n+1):
    arr[i].sort()


def bfs(x):
    q = deque([x])
    visit = [-1] * (n+1)
    visit[x] = 0
    while q:
        x = q.popleft()
        
        for next in arr[x]:
            if visit[next] == -1:
                visit[next] = visit[x] + 1
                q.append(next)
                
    return visit

distances = bfs(1)

min_costs = [1] + [0] * n
for i in range(2,n+1):
    if distances[i] == -1:
        continue

    min_costs[distances[i]] += 1

res = 1
for min_cost in min_costs:
    if min_cost == 0:
        continue
    
    res *= (min_cost + 1)

res -= 1
print(res%1000000007)

'''
틀린 이유
실시간 충돌을 고려하지 않고 도착지점에서의 충돌만 고려했기 때문
time이라는 것을 도입하여 bfs 순회하면서 저장해둔다
1-4-5-6

1-2-3-5-7

이 경우 1시간 뒤 5번에서 충돌한다.

그리고 낮은 간선부터 돌려면 정렬을 해야함
'''