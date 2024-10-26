def solution(targets):
    sorted_targets = sorted(targets, key = lambda x: (x[1], x[0]))
    end = 0
    answer = 0
    for target in sorted_targets:
        start = target[0]
        if start >= end:
            answer += 1
            end = target[1]
    
    return answer