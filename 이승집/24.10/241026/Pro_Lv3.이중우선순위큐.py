import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for i in operations:
        m, num = i.split()
        if m == "I":
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        elif m == "D" and num == "-1" and min_heap:
            m = heapq.heappop(min_heap)
            max_heap.remove(-m)
        elif m == "D" and num == "1" and max_heap:
            M = heapq.heappop(max_heap)
            min_heap.remove(-M)

    if min_heap:
        answer = [max(min_heap), min(min_heap)]
    else:
        answer = [0, 0]
    return answer


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
