# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
# 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.



# 내 풀이 deque사용
from collections import deque
def solution(s):
    answer = True
    sdq = deque(s)  # dq선언
    nowdq = deque()
    while sdq:  # sdq가 빌때까지 반복
        if not nowdq:  # 만약 현재의 dq가 비어있다면 새로추가
            nowdq.append(sdq.popleft())
        elif sdq[0] != nowdq[0]:
            sdq.popleft()
            nowdq.popleft()
        else:  # 그 외의 경우 즉 일치할 경우 추가
            nowdq.append(sdq.popleft())
            
        if nowdq and nowdq[0] == ')':  # 괄호가 완성되지 않는 경우를 예외처리
            break
            
    if nowdq:  # 만약 다 비워내지 못하면 실패
        answer = False

    return answer


# deque안쓴 깔끔한 코드
def solution(s):
    stack = []
    for i in s:
        # 스택이 비어있는데 닫힌괄호 들어오는 경우 False return
        if len(stack) == 0 and i == ')':
            return False

        # 스택 맨 위에 열린괄호 있는데 닫힌괄호 들어오는 경우: pop
        if i == ')' and stack[-1] == '(':
            stack.pop()

        # 열린 괄호 들어오는 경우 stack에 append
        if i == '(':
            stack.append('(')

    # 다 끝났는데 남아있으면 False return
    return False if len(stack) != 0 else True