from collections import Counter


def solution(weights):

    comb = [(2, 1), (3, 2), (4, 3)]
    weight_count = Counter(weights)
    answer = 0
    print(weight_count)
    
    # 같은 수
    for i in weight_count:
        if weight_count[i] > 1:
            answer += weight_count[i] * (weight_count[i] - 1) // 2

    # 다른 수
    for i in weight_count:
        for j, k in comb:
            other_weight = i * j // k
            if i * j % k == 0 and other_weight in weight_count:
                answer += weight_count[i] * weight_count[other_weight]

    return answer

print(solution([100, 180, 360, 100, 270]))