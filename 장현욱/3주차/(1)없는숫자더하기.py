# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.


def solution(numbers):
    answer = -1
    allnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in numbers:
        if i in allnumbers:
            allnumbers.remove(i)
    answer = sum(allnumbers)
    return answer

