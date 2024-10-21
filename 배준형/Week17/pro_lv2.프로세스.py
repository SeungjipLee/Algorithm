from collections import defaultdict

def solution(priorities, location):
    answer = 0
    # [] 순번 부여
    n = len(priorities)
    nums = sorted(list(set(priorities)), reverse=True)
    rank = defaultdict(int)
    rank_num = 1
    for num in priorities:
        rank[num] += 1
    
    ranks = [0] * n
    rank_num = 1
    idx = 0
    for i in range(len(nums)):
        target = nums[i]
        cnt = 0
        while True: 
            if priorities[idx] == target:
                ranks[idx] = rank_num
                rank_num += 1
                rank[target] -= 1
            idx += 1
            cnt += 1
            if rank[target] == 0:
                break
            if cnt == n:
                break
            if idx == n:
                idx = 0
            
    return ranks[location]