import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    
    while True:
        a = heapq.heappop(h)
        if a < K and h:
            b = heapq.heappop(h)
            answer += 1
            heapq.heappush(h, a+b*2)
        else:
            heapq.heappush(h, a)
            break
    
    if h[0] >= K:
        return answer
    else:
        return -1