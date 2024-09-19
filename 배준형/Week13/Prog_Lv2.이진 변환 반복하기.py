def solution(s):
    answer = [0, 0]
    
    
    
    while True:
        tmp = ""
        cnt = 0
        # print("s = ", s)
        for i in s:
            if i == "1":
                cnt += 1
            else:
                answer[1] += 1
        # print("cnt = ", cnt)
        while cnt != 0:
            if cnt % 2:
                tmp = "1"+ tmp
            else:
                tmp = "0"+ tmp
            cnt //= 2
        # print(tmp)
        s = tmp
        answer[0] += 1
        if s == "1":
            break
        
    return answer
