from collections import defaultdict

def solution(participant, completion):
    answer = ''
    d = defaultdict(int)
    for p in participant:
        d[p] += 1
    for c in completion:
        d[c] -= 1
    
    for p in d:
        if d[p]:
            answer = p
    return answer