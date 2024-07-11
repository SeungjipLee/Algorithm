def solution(operations):
    heap = []
    
    for o in operations:

        order, num = o.split()
        num = int(num)
        if order == "I":
            heapq.heappush(heap, num)
        elif heap and order == "D":
            if num == -1:
                heapq.heappop(heap)
            elif num == 1:
                max_value = max(heap)
                heap.remove(max_value)
    answer = [0, 0]

    if heap:
        answer = [max(heap), heap[0]]
    return answer