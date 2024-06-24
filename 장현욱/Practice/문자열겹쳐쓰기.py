def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer


# 슬라이싱을 통해 문자열 겹치기