from collections import deque


def solution(n, computers):
    answer = 0
    q = deque()
    visited = [0] * n
    
    for i in range(n):
        # print(i, visited)
        if visited[i]:
            continue
        answer += 1
        q.append(i)
        
        while q:
            now = q.popleft()
            visited[now] = 1
            for nxt in range(n):
                if visited[nxt]:
                    continue
                if computers[now][nxt] == 0:
                    continue
                q.append(nxt)
            
    return answer