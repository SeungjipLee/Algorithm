import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        low = []
        for _ in range(2):
            low.append(heapq.heappop(scoville))

        heapq.heappush(scoville, low[0] + low[1] * 2)
        answer += 1

    return answer