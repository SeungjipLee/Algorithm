from collections import deque

def solution(n, wires):
    answer = 1000

    # 1번부터 시작해서 부모(1번은 부모가 없음)빼고 자기 자식이 몇명인지 모두 확인함
    # BFS로 전체를 도는데 
    # 부모 제외한 상태에서 BFS 를 돌아서 자식 수 셈
    # 2중 BFS
    adj_ls = [[] for _ in range(n+1)]
    
    for wire in wires:
        a, b = wire
        adj_ls[a].append(b)
        adj_ls[b].append(a)
    
    childs = [1] * (n+1)
    q = deque()
    visited = [0] * (n+1)
    q.append(1)
    
    while q:
        now = q.popleft()
        visited[now] = 1
        childs[now] = BFS(visited, now, adj_ls)
        for nxt in adj_ls[now]:
            if visited[nxt]:
                continue
            q.append(nxt)
    for child in childs:
        answer = min(answer, abs(n - child * 2))
    return answer

def BFS(visit, s, adj):
    v = []
    for vi in visit:
        v.append(vi)
    cnt = 0 
    que = deque()
    que.append(s)
    
    while que:
        a = que.popleft()
        v[a] = 1
        cnt += 1
        for nxt in adj[a]:
            if v[nxt]:
                continue
            que.append(nxt)
    return cnt