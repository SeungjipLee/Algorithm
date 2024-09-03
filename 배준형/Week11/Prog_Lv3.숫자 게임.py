def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    n = len(A)
    i, j = n-1, n-1
    while i >= 0:
        if B[j] > A[i]:
            j -= 1
            i -= 1
            answer += 1
            continue
        i -= 1
        
    return answer