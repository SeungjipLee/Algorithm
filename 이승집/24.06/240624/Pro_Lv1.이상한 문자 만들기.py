'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

[제한 사항]
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
'''

# s는 주어집니다.
s = "try hello world"

answer = []
word = []
is_word = False  # 현재 문자가 단어의 일부인지를 판단

for char in s:
    if char == ' ':
        if is_word:  # 단어를 마무리하고 저장
            answer.append(''.join(word))
            word = []
            is_word = False
        answer.append(' ')  # 공백을 결과에 추가
    else:
        if not is_word:  # 새 단어의 시작
            is_word = True
        # 짝수 인덱스면 대문자, 홀수 인덱스면 소문자로 변환
        if len(word) % 2 == 0:
            word.append(char.upper())
        else:
            word.append(char.lower())

    # 마지막 단어 처리
if word:
    answer.append(''.join(word))

print(''.join(answer))
