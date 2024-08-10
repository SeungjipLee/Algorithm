# 중위 표기식을 후위 표기식으로 변경하기
# A + B / C * R - Q
# (A + ((B / C) * R)) - Q
# A + BC/R* - Q
# ABC/R*+Q-
# A + B / (C + D) * (R - Q) - T
# A + BCD+/RQ-* - T
# ABCD+/RQ-*+T-

# A+(B+((D + V * (C + D / ( E * C )) + K))
# ABDVCDEC*/+*+K+++
# A  +  (  B  +  a  )
# a = (  c  +  K  )
# c = (  D  +  b  )
# b = V  *  (  C+D  /  (E*C) )
## 로직
# 전처리 = 괄호있는거 일단 다 해소시켜 놓기
# 후위표기식으로 만들기


# 필요한 함수
# 연산자를 만났을 때 처리
# 괄호 없애는 처리

# 숫자를 만난다
# 다음 연산자보기
# + - 이면 스택에 넣기
# * / 이면 두개 꺼내서 연산하고 집어넣기
import sys
from collections import deque
input_ = sys.stdin.readline

infix = input_().rstrip()
q = deque(list(infix))

# 후위 표기식 만들기
def make_postfix():
    num_stack = []
    operator_stack = []
    while q:
        now = q.popleft()
        
        # 여는 괄호 시 재귀함수 호출
        if now == "(":
            now = make_postfix()
        # 닫는 괄호 시 stack 의 top을 반환
        elif now == ")":
            return num_stack.pop()
        # 더하기와 빼기는 연산자 스택에 추가
        elif now in "+-":
            operator_stack.append(now)
            continue
        # 곱하기와 나누기는 스택의 탑과 다음 항을 불러와 바로 연산
        elif now in "*/":
            nxt = q.popleft()
            if nxt == "(":
                nxt = make_postfix()
            num_stack.append(num_stack.pop()+nxt+now)
            continue
        
        # 피연산자 스택에 아무것도 없다면 현재값을 추가
        if not num_stack:
            num_stack.append(now)
            continue
        
        # 여기까지 왔다는 것은 + 혹은 - 연산을 진행해야 할 차례
        # 다음 항에 곱하기 혹은 나누기 연산이 있을 수 있으므로
        # 가능한 만큼 연산하기
        while q:  
            op = q.popleft()
            if op in "*/":
                nxt = q.popleft()
                if nxt == "(":
                    nxt = make_postfix()
                now = now+nxt+op
            else:
                q.appendleft(op)
                break
        
        # 더하기, 빼기를 들고와 연산 후 스택에 다시 저장
        if operator_stack:
            num_stack.append(num_stack.pop()+now+operator_stack.pop())
    
    # 결과물 반환
    return num_stack[0]

print(make_postfix())
# import sys
# from collections import deque
# input_ = sys.stdin.readline

# num_stack = []
# operator_stack = []
# infix = input_().rstrip()
# q = deque(list(infix))

# def make_postfix(op): # op = * or /
#     a = num_stack.pop()
#     operator = op
#     b = q.popleft()
#     # print("make", a, operator, b)
#     if b == "(":
#         b = solve_parenthesis()
#         q.popleft()
#     num_stack.append(a+b+operator)
#     return
    

# def solve_parenthesis(): # operator 가 + - 인 경우 다음 것도 확인해야 함
#     a = q.popleft()
#     if a == "(":
#         a = solve_parenthesis()
#         q.popleft()
        
#     operator = q.popleft()
#     if operator == ")":
#         q.appendleft(operator)
#         return a
#     b = q.popleft()
#     # print("solve", a, operator, b)
#     if b == "(":
#         b = solve_parenthesis()
#         q.popleft()
    
#     while q:
#         nxt = q.popleft()
#         if nxt in "*/":
#             num_stack.append(b)
#             make_postfix(nxt)
#             b = num_stack.pop()
#         else:
#             q.appendleft(nxt)
#             break    
    
#     return a+b+operator

# while q:
#     now = q.popleft()
#     if now in "+-":
#         operator_stack.append(now)
#         continue
#     elif now in "*/":
#         make_postfix(now)
#         continue
#     elif now == "(":
#         now = solve_parenthesis()
#         q.popleft()
#     if not num_stack:
#         num_stack.append(now)
#         continue
    
#     # 다 지나왔다면 건너편 확인
#     while q:
#         nxt = q.popleft()
#         if nxt in "*/":
#             num_stack.append(now)
#             make_postfix(nxt)
#             now = num_stack.pop()
#         else:
#             q.appendleft(nxt)
#             break
    
#     if operator_stack:
#         num_stack.append(num_stack.pop()+now+operator_stack.pop())
    
    
# print(num_stack[0])
    
