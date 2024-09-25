from collections import deque
from copy import deepcopy
def solution(s):
    answer = 0
    n = len(s)
    q = deque(list(s))
    
    for i in range(n):
        valid, c = is_valid(q)
        if valid:
            answer = c
            break
        else:
            q.append(q.popleft())

    return answer

def is_valid(dq):
    dq = deepcopy(dq)
    stack = []
    cnt = 0
    while dq:
        now = dq.popleft()
        if not stack:
            cnt += 1
            stack.append(now)
            continue
        if now in "([{":
            stack.append(now)
            continue
        if stack:
            if now == ")" and stack[-1] == "(":
                stack.pop()
            elif now == "]" and stack[-1] == "[":
                stack.pop()
            elif now == "}" and stack[-1] == "{":
                stack.pop()
    
    if stack:
        return False, cnt
    return True, cnt