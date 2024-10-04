import re
from itertools import permutations
from collections import deque


def calculate(s, a, b):
    if s == "*":
        return a * b
    elif s == "+":
        return a + b
    else:
        return a - b


def solution(expression):
    answer = 0
    cal = ["+", "-", "*"]
    nums = [int(i) for i in re.split(r'[-+*]', expression)]
    cals = [i for i in expression if i in cal]
    print(nums, cals)
    for i in permutations(cal, 3):
        fir, sec, thi = i
        stack = []
        mid = 0
        for j in range(len(nums)):
            if len(stack) >= 1 and stack[-1] == fir:
                stack.append(calculate(stack.pop(), stack.pop(), nums[j]))
            else:
                stack.append(nums[j])
            if j == len(nums) - 1:
                break
            stack.append(cals[j])

        Q = deque(stack)
        stack2 = []
        while Q:
            S = Q.popleft()
            if stack2 and stack2[-1] == sec:
                stack2.append(calculate(stack2.pop(), stack2.pop(), S))
            else:
                stack2.append(S)
        Q2 = deque(stack2)
        mid = Q2.popleft()
        while Q2:
            N = Q2.popleft()
            if N == thi:
                continue
            else:
                mid = calculate(thi, mid, N)

        if abs(mid) > answer:
            answer = abs(mid)

    return answer