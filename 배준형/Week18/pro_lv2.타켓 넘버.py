from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    
    while q:
        num, depth = q.popleft()
        if depth == n-1:
            if num == target:
                answer += 1
            continue
        q.append([num+numbers[depth+1], depth+1])
        q.append([num-numbers[depth+1], depth+1])
    return answer

        
        
    