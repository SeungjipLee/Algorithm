from collections import deque


def solution(prices):
    N = len(prices)
    answer = [-1] * N
    mid = []

    for idx, price in enumerate(prices):
        mid.append((price, idx))

    mid.sort()
    mid = deque(mid)

    while mid:
        now = mid.popleft()
        k = -1
        for j in range(now[1], N):
            k += 1
            if answer[j] != -1:
                break
        answer[now[1]] = k

    return answer