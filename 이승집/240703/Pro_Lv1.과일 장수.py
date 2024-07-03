def solution(k, m, score):
    li = sorted(score, reverse=True)
    answer = 0
    l = len(score) // m
    for i in range(l):
        st = li[m * i: m * (i + 1)]
        answer += min(st) * m

    return answer

