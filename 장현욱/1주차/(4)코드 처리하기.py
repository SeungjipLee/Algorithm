# 문자열 code가 주어짐
# 앞에서부터 읽으면서 문자가 1 이면 mode를 바꿈
# mode의 상태에 따라 code를 읽어서 ret을 만들기
# mode는 0과1존재
# idx를 0부터 len(code-1) 까지1씩 키워나가면서
# code[idx]의 값에 따라 다음과 같이 행동

# mode가 0일때
# code[idx]가 1이 아니면 idx가 짝수일때만 ret의 맨 뒤에 code[idx] 추가
# code[idx]가 1이면 mode를 0에서1로 바꾸기

# mode가 1일때
# 홀수
# 1에서0으로

# 시작할때 mode는0, 만약 ret가 빈 문자열이면 "EMPTY" 리턴

# code의 길이 = 1~100,000
# code는 알파벳 소문자 또는 1 로 이루어짐

def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
      if mode == 0:
        if code[i] == '1':
            mode = 1 
        else:
            if i == 0 or i % 2 == 0:
              ret += code[i]

      else :
        if code[i] == '1':
            mode = 0
        else : 
            if i % 2 == 1:
              ret += code[i]
    
    if ret == '':
      ret = 'EMPTY'
    return ret