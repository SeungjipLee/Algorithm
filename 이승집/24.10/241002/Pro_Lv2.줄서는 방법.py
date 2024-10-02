"""
from itertools import permutations

def solution(n, k):
    l = 1
    for i in permutations(range(1, n+1), n):
        if l == k:
            return list(i)
        l += 1

완탐 => 시간 초과
"""


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


def solution(n, k):
    result = []
    num_list = [i for i in range(1, n + 1)]
    while (n != 0):
        num_case = factorial(n - 1)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            result.append(num_list.pop(idx - 1))
        else:
            result.append(num_list.pop(idx))
        n -= 1
    return result
