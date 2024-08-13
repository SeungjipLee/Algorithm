import sys
sys.stdin = open("Boj_1260.txt")

from collections import deque

N, M, V = map(int, input().split())

# 이중리스트로 연결정보 담기
Board = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 연결
    Board[a].append(b)
    Board[b].append(a)

# 인접 리스트를 오름차순으로 정렬 (작은 노드부터 방문하기 위함)
for edges in Board:
    edges.sort()


# DFS 함수 정의
def dfs(node, visited):
    # 현재 노드를 방문 처리하고 출력
    visited[node] = True
    print(node, end=' ')

    # 인접한 노드들에 대해
    for neighbor in Board[node]:
        if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
            dfs(neighbor, visited)  # 그 노드를 방문
            if False not in visited:
                return


# 방문 여부를 확인할 리스트
visited = [False] * (N + 1)
visited2 = [False] * (N + 1)
visited[0] = True
# DFS 탐색 시작
dfs(V, visited)

def bfs(node, visited):
    Q = deque([node])
    visited[node] = True
    while Q:
        now = Q.popleft()
        print(now, end=' ')
        for next in Board[now]:
            if visited[next] == False:
                Q.append(next)
                visited[next] = True
    return
print("")
bfs(V, visited2)