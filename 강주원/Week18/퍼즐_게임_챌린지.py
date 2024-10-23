def solution(diffs, times, limit):
    diffandtime = []
    n = len(diffs)
    for i in range(n):
        diffandtime.append([diffs[i], times[i]])
    
    diffandtime.sort()
    def get_spend_time(level):
        spend_time = times[0]
        for i in range(1, n):
            diff, time_cur, time_prev = diffs[i], times[i], times[i-1]
            if diff <= level:
                spend_time += time_cur
            else:
                wrong_cnt = diff - level
                spend_time += wrong_cnt * (time_prev + time_cur) + time_cur
        
        return spend_time
    
    
    def binary_search(start, end):
        res = 100000
        while start <= end:
            mid = (start+end) // 2
            spend_time = get_spend_time(mid)
            if spend_time <= limit:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return res
    
    answer = binary_search(1, 100000)
    return answer