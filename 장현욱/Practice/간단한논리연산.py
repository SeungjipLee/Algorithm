# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

# (x1 ∨ x2) ∧ (x3 ∨ x4)

def solution(x1, x2, x3, x4):
    a = True
    b = True
    answer = True
    if x1 == x2:
        a = x1
    elif x1 != x2:
        a = True
    if x3 == x4:
        b = x3
    elif x3 != x4:
        b = True    
    if a == b:
        answer = a
    elif a != b:
        answer = False
    return answer