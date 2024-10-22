n = 6
times = [7, 10]


def solution(n, times):
    start, end = 1, max(times) * n
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in times:
            cnt += mid // i

        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer