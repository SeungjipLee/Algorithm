def solution(sizes):
    # 1. 전체중에서 가장 큰 값을 찾기
    # 2. 리스트 두개중 더 작은값만 모은 후 그중 가장 큰 값 찾기
    best = []
    second = []
    answer = 0
    for i in sizes:
        best.append(max(i))
        second.append(min(i))
    answer = max(best) * max(second)
    return answer