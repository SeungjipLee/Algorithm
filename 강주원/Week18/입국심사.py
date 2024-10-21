def solution(n, times):
    def binary_search(start, end, target):
        res = max(times)*n
        while start <= end:
            mid = (start+end) // 2
            cnt = get_count(mid, times)
            if cnt >= target:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1

        return res
            

    def get_count(num, times):
        cnt = 0
        for time in times:
            cnt += num // time

        return cnt

    res = binary_search(0, max(times)*n, n)
    return res