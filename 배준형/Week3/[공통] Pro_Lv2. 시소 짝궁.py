def solution(weights):
    answer = 0
    # 100000 개 중 임의의 2개를 뽑아서 균형을 맞출 수 있는지..
    w_dict = {}
    for w in weights:
        if w_dict.get(w):
            w_dict[w] += 1
        else:
            w_dict[w] = 1
    # print(w_dict)
    
    # 후보군들 1 2/3 1/2 3/2 3/4 4/3 2
    candi = [[] for _ in range(1001)]
    for i in range(100, 1001):  
        candi[i].append(i)
        
        if i % 2 == 0:
            a = i // 2 * 3
            b = i // 2
            if 100 <= a <= 1000:
                candi[i].append(a)
            if 100 <= b <= 1000:
                candi[i].append(b)
        
        if i % 3 == 0:
            a = i // 3 * 2
            b = i // 3 * 4
            if 100 <= a <= 1000:
                candi[i].append(a)
            if 100 <= b <= 1000:
                candi[i].append(b)
                
        if i % 4 == 0:
            a = i // 4 * 3
            if 100 <= a <= 1000:
                candi[i].append(a)
                
        if 100 <= 2*i <= 1000:
            candi[i].append(2*i)
                 
    for w in range(100, 1001):
        # 있는 것만 조회
        if w_dict.get(w):
            # 있다면 짝궁 찾기
            for c in candi[w]:
                # 자기 보다 무거운 후보군만 비교하면됨 앞에서 이미 낮은건 했기 때문
                if c < w:
                    continue
                # 짝궁 후보군이 존재한다면 더해주기
                if w_dict.get(c):
                    # 후보군이 자기자신인 경우
                    if w == c and w_dict[c] >= 2:
                        answer += w_dict[w] * (w_dict[w] - 1) // 2
                    elif w != c:
                        # print(w, c)
                        answer += w_dict[c] * w_dict[w]

    
    return answer