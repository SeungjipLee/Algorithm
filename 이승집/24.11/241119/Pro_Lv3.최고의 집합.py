def solution(n, s):
    if n > s:
        return [-1]

    r = s % n
    m = s // n
    mid = [m] * n
    for i in range(r):
        mid[n - 1 - i] += 1
    return mid