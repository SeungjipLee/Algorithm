from collections import deque

N = int(input())

"""
타일의 종류 : 00 or 1 2가지

N = 1인 경우 => 1로 1가지
N = 2인 경우 => 00, 11로 2가지
N = 3인 경우 => 100 or 001 or 111 으로 3가지
N = 4인 경우 => 0000 1100, 1001 0011, 1111

1, 2, 3, 5, 8, 13, 21

메모이제이션 => 메모리 초과
큐 => 시간 초과
"""

if N <= 2:
    print(N)
else:
    a, b = 1, 2
    for _ in range(3, N + 1):
        a, b = b % 151746, (a + b) % 151746
    print(b)