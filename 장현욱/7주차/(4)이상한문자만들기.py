# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.


def solution(s):
    answer = ''
    index = 0
    
    for char in s:
        if char == ' ':
            answer += ' '
            index = 0  # 공백을 만나면 인덱스를 초기화하여 새로운 단어로 인식
        else:
            if index % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            index += 1
            
    return answer