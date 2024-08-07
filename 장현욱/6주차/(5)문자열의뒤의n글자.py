#문자열 my_string과 정수 n이 매개변수로 주어질 때,
#  my_string의 뒤의 n글자로 이루어진 문자열을 return 하는
#  solution 함수를 작성해 주세요.

def solution(my_string, n):
    return my_string[len(my_string)-n:]

print(solution('ProgrammerS123', 11))

# 문자열 원하는 칸부터 시작하는법