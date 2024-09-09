def solution(s):
    l = len(s)
    answer = len(s)
    for i in range(1,l+1):
        init = s[:i]
        cnt = 1
        S = ''
        j = 0
        for j in range(1, l//i):
            unit = s[i*j:i*(j+1)]
            if unit == init:
               cnt += 1 
            else:
                num = ''
                if cnt > 1:
                    num = str(cnt)
                    
                S += num + init
                init = unit
                cnt = 1
                
        num = ''
        if cnt > 1:
            num = str(cnt)
        S += num + init + s[i*(j+1):]
        answer = min(answer, len(S))
        
    
    return answer