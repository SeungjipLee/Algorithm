from collections import deque

def solution(n, wires):
    res = 1e9
    for i in range(n-1):    
        visit = [0] * (n+1)
        graph = [[] for _ in range(n+1)]
        new_wires = wires.copy()
        new_wires.pop(i)
        for wire_a, wire_b in new_wires:
            graph[wire_a].append(wire_b)
            graph[wire_b].append(wire_a)

        cnt = bfs(graph, wires[0][0], visit)
        res = min(res, abs(2*cnt - n))

    answer = -1
    return answer


def bfs(graph, start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for node in graph[v]:
            if not visit[node]:
                q.append(node)
                visit[node] = 1

    return cnt     

    
