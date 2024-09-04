def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    while True:
        if n == 0:
            break
        elif n == 1:
            answer.append(s)
        else:
            answer.append(s//n)
            s -= s//n
        n -= 1
        
    
    return sorted(answer)