from collections import deque
def solution(elements):
    answer = {}
    q = deque(elements)
    N = len(elements)
    
    for i in range(N):
        s = q[0]
        answer[s] = True
        for j in range(1, N):
            s += q[j]
            answer[s] = True
        
        q.append(q.popleft())
    
    return len(answer)
