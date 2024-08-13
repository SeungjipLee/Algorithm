# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
def solution(a, b):
    answer = 0
    ab = [a,b]
    ab.sort()
    for i in range(ab[0], ab[1]+1):
        answer += i
    return answer