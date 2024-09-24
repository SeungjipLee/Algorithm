from collections import defaultdict
import heapq

def solution(k, tangerine):
    answer = 0
    tangerines = defaultdict(int)
    h = []
    for t in tangerine:
        tangerines[t] += 1
    
    for t in tangerines:
        heapq.heappush(h, [-tangerines[t], t])

    for i in range(len(h)):
        if k <= 0:
            break
        answer += 1
        cnt, t = heapq.heappop(h)
        k += cnt
    
    return answer