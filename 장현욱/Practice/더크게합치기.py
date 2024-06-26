# 두 숫자를 붙여서 새로운 숫자를 만드세요
# ex) 3 + 12 = 312
# 그리고 두개의 숫자중 가장 큰 수를 출력

def solution(a, b):
    answer = 0
    case1 = int(str(a) + str(b))
    case2 = int(str(b) + str(a))

    if case1 >= case2:
        answer = case1
    else :
        answer = case2

    return answer