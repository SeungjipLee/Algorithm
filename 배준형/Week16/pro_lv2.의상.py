from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = len(clothes)
    d = defaultdict(int)
    
    for cloth in clothes:
        d[cloth[1]] += 1
    
    for i in range(2, len(d)+1):
        
        for comb in combinations(d, i):
            tmp = 1
            for c in comb:
                tmp *= d[c]
            answer += tmp
    return answer