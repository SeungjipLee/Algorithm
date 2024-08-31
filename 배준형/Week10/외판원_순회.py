import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# dp 저장 방식
# dp[i][j] = val, i 는 현재노드 j 는 방문한 노드들 정보, val은 방문안한 노드를 전부 순회하고 시작점으로 돌아가는 최소비용
# ex) N=4, dp[3][1111] 노드가 4개고 현재노드 3번, 이미모든 노드를 방문함, 3번노드에서 0번노드로 가는 비용만 저장하면 됨
# 결국 알고자하는건 dp[0][0001] 이 어떤 값을 가지고 있냐 0번노드를 제외하고 모든 노드를 돌고와서 저장된 최소비용

N = int(input_())
dp = defaultdict(dict)
graph = [list(minput()) for _ in range(N)]
for i in range(1, N):
    dp[i][2**N-1] = graph[i][0]
    
print(dp)
answer = int(1e9)

def find_route(now, visited):
    global answer
    print(now, visited)
    if dp[now].get(visited) != None:
        return dp[now][visited]
    
    for i in range(N):
        if visited & 1<<i:
            continue
        dp[i][visited] = find_route(i, visited|1<<i) + graph[now][i]
    
    return dp[now][visited]
# 0 1 2 3->0


dp[0][1] = find_route(0, 1)
print(dp)
print(dp[0][1])