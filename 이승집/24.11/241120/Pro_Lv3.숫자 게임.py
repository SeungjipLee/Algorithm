def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    a = b = 0
    n = len(A)
    while True:
        if b == n:
            break
        if A[a] < B[b]:
            a += 1
            answer += 1
        b += 1
    return answer