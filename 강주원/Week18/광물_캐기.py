def solution(picks, minerals):
    minerals_num = len(minerals)
    minerals_cnt = []
    pick_cnt = sum(picks)
    
    for i in range(0, min(minerals_num, pick_cnt*5), 5):
        mineral_cnt = {"stone": 0, "iron": 0, "diamond": 0}
        for mineral in minerals[i:i+5]:
            mineral_cnt[mineral] += 1
        
        minerals_cnt.append([i for i in mineral_cnt.values()])
    
    
    minerals_cnt.sort(key=lambda x:(x[2], x[1], x[0]), reverse = True)
    answer = 0
    for i in minerals_cnt:
        if picks[0] > 0:
            answer += sum(i)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += i[0] + i[1] + i[2] * 5
            picks[1] -= 1
        elif picks[2] > 0:
            answer += i[0] + i[1] * 5 + i[2] * 25
            picks[2] -= 1
        
            
    return answer

print(solution([0, 0, 1], ["stone", "stone", "stone", "stone", "stone", "iron", "iron", "iron", "iron", "iron"]))