import heapq

def solution(jobs):
    n = len(jobs)
    answer = 0
    h = []
    # 현재 시간보다 시작 시간이 빠르거나 같은 작업들을 힙에 넣기
    time = 0
    
    jobs.sort(key=lambda x: x[0])
        
    time = 0
    idx = 0
    while time <= 1_000_000:
        # print(time, answer)
        while idx < n and jobs[idx][0] <= time:
            a, b = jobs[idx]
            heapq.heappush(h, [b, a])
            idx += 1
        
        if h:
            b, a = heapq.heappop(h)
            answer += time+b - a
            time += b
        else:
            time += 1
    
    return answer//n