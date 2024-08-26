import math
def solution(k, d):
    # (a** + b**)(1/2) 또는 math.sqrt(a** + b**)
    answer = 0
    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            if d >= math.sqrt(i**2 + j**2):
                answer += 1
            else:
                break
    return answer