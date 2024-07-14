def solution(n, works):
    len_works = len(works)
    answer = 0
    works = sorted(works)
    total = sum(works) - n
    if total <= 0:
        return 0
    
    for work in works:
        if work < total / len_works:
            total -= work
            answer += work ** 2
        else:
            done = work - total // len_works
            work -= done
            total -= work
            answer += work ** 2
        len_works -= 1
    
    return answer