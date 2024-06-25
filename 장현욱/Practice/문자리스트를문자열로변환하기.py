# 문자들이 담겨있는 배열 arr가 주어집니다. 
# arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer