# 두 숫자를 이어붙여서 씉값반환
# a+b 또는 2 * a * b 중 더 큰 값을 반환

def solution(a, b):
    answer = 0
    case1 = int(str(a) + str(b))
    case2 = 2 * a * b

    if case1 > case2:
        answer = case1
    else:
        answer = case2
    return answer