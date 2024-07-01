def solution(k, score):
    answer = []

    for i in range(len(score)):
        mid = score[:i + 1]
        mid.sort()
        if len(mid) >= k + 2:
            answer.append(mid[-k])
        elif len(mid) == k + 1:
            answer.append(mid[1])
        else:
            answer.append(mid[0])

    return answer
