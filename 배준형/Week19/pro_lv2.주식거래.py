from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0] * n
    q = deque()
    
    for idx, price in enumerate(prices):
        tmp = deque()
        while q:
            i, num, d = q.popleft()

            if price >= num:
                tmp.append([i, num, d+1])
            else:
                answer[i] = d+1
        q = tmp
        q.append([idx, price, 0])
        # print(q)
        
    while q:
        i, num, d = q.popleft()
        answer[i] = d
    return answer