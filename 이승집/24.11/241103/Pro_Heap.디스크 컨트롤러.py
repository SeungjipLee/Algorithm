import heapq


def solution(jobs):
    jobs.sort()
    current_time = 0
    sum_time = 0
    n = len(jobs)

    H = []
    i = 0

    while i < n or H:
        while i < n and jobs[i][0] <= current_time:
            heapq.heappush(H, (jobs[i][1], jobs[i][0]))
            i += 1
        if H:
            duration, start = heapq.heappop(H)
            sum_time += duration + current_time - start
            current_time += duration
        else:
            current_time = jobs[i][0]

    return sum_time // n