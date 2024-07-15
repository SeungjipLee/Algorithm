def solution(users, emoticons):
    # 할인율은 10, 20, 30 , 40 중 하나로 설정
    # 유저는 특정 할인율 이상인 것을 모두 구매
    # 모두 구매한다 했는데 비싸면 구독
    # 1. 최대한 구독을 많이
    # 2. 판매액을 많이
    # 1637,4100
    total_sales = 0
    total_subs = 0
    
    ratio = [10, 20, 30, 40]
    len_e = len(emoticons)
    emo_ratio = [0] * len_e
    
    # 완전탐색
    i = 0
    idx = 0
    while True:
    # for k in range(16):
        
        cur = []
        for j in range(len_e):
            cur.append([ratio[emo_ratio[j]], emoticons[j] * (100 - ratio[emo_ratio[j]]) // 100])
            
        total_tmp = 0
        sub_tmp = 0
        
        for user in users:
            r, m = user
            tmp = 0
            for c in cur:
                if r <= c[0]:
                    tmp += c[1]
            if tmp >= m:
                sub_tmp += 1
            else:
                total_tmp += tmp
            
        if total_subs == sub_tmp:
            total_sales = max(total_sales, total_tmp)
        elif total_subs < sub_tmp:
            total_subs = sub_tmp
            total_sales = total_tmp


        # print(emo_ratio[1])
        while emo_ratio[i] == 3:
            # print("다음인덱스 올리세요")
            emo_ratio[i] = 0
            i += 1
            if i == len_e:
                break
            
        if i == len_e:
            break
        # 일단 첫번째꺼 올림
        emo_ratio[i] += 1
        i = 0
        
        # print(emo_ratio)
    
    answer = [total_subs, total_sales]
    return answer