def solution(n, left, right):
    answer = []
    
    i = left // n
    j = left % n
    cnt = 0
    
    while True:
        cnt += 1
        answer.append(max(i,j)+1)
        
        if cnt == right-left+1:
            break
            
        j += 1
        if j == n:
            i += 1
            j = 0
            
    return answer