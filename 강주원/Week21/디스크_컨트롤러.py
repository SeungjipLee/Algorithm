import heapq
from collections import deque

def solution(jobs):
    hq = []
    length = len(jobs)
    jobs.sort()
    now = jobs[0][0]
    answer = 0
    jobs = deque(jobs)
    heapq.heappush(hq, jobs.popleft()[::-1])
    
    while hq:
        job = heapq.heappop(hq)
        now += job[0]
        answer += now - job[1]
        if not hq and jobs and jobs[0][0] > now:
            now = jobs[0][0]

        while jobs:
            if jobs[0][0] > now:
                break

            heapq.heappush(hq, jobs.popleft()[::-1])
    
    answer //= length
    return answer

print(solution([[1, 3], [0, 15], [1,15], [5,3]]))
print((15+17+12+35)//4)