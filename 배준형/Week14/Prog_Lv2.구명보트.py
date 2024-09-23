def solution(people, limit):
    answer = 0
    weighs = [0] * 241
    for p in people:
        weighs[p] += 1
    
    people.sort(reverse=True)

    for p in people:
        if not weighs[p]:
            continue
        answer += 1
        # print("무게가 ", p)
        weighs[p] -= 1
        remain = limit - p
        
        while True:
            for w in range(remain, 0, -1):
                if weighs[w]:
                    # print(w)
                    weighs[w] -= 1
                    remain -= w
                    break
            else:
                break
    
    
    return answer