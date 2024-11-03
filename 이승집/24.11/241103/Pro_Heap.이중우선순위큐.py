import heapq as hq


def solution(operations):
    max_H = []
    min_H = []
    for operation in operations:
        a, b = operation.split()
        if a == "I":
            hq.heappush(min_H, int(b))
            hq.heappush(max_H, -int(b))
        else:
            # 최댓값 삭제
            if max_H and b == "1":
                mid = hq.heappop(max_H)
                min_H.remove(-mid)
            # 최솟값 삭제
            elif max_H and b == "-1":
                mid = hq.heappop(min_H)
                max_H.remove(-mid)

    if min_H:
        answer = [max(min_H), min(min_H)]
    else:
        answer = [0, 0]

    return answer