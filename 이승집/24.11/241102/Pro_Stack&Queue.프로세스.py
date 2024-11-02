from collections import deque

def solution(priorities, location):
    D = []
    for idx, priority in enumerate(priorities):
        D.append((priority, idx))
    D = deque(D)
    cnt = 1
    while D:
        pri, idx = D.popleft()
        if D:
            M = max([i[0] for i in D])
            if pri >= M:
                if idx == location:
                    return cnt
                else:
                    cnt += 1
            else:
                D.append((pri, idx))
        else:
            return cnt