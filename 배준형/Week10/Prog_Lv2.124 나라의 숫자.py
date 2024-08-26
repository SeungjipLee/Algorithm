def solution(n):
    answer = ''
    nara = ["1", "2", "4"]
    i = 1
    length = 1
    # 25 -3-9 = 13 -9 = 4
    while True:
        if n - 3**i > 0:
            n -= 3**i
            i += 1
            length += 1
            continue
        i -= 1
        break
    # print(n, length, i)
    
    if length > 1:
        idx = 0
        while True:
            if n - 3**i > 0:
                n -= 3**i
                idx += 1
            else:
                answer += nara[idx]
                break
    i -= 1
    # print(n, length, i, answer)
    idx = 0
    while i > 0:
        
        if n > 3**i > 0:
            idx += 1
            n -= 3**i
            continue
        else:
            i -= 1
            answer += nara[idx]
            idx = 0
        
    answer += nara[n-1]
    return answer

for i in range(1, 30):
    print(solution(i))