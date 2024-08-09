import sys
from collections import deque
input_ = sys.stdin.readline

while True:
    num_stack = []
    operator_stack = []
    infix = input_().rstrip()
    if infix == "0":
        break
    q = deque(list(infix))

    def make_postfix(op):
        a = num_stack.pop()
        operator = op
        b = q.popleft()
        # print("make", a, operator, b)
        if b == "(":
            b = solve_parenthesis()
            q.popleft()
        num_stack.append(a+b+operator)
        return
        

    def solve_parenthesis():
        a = q.popleft()
        operator = q.popleft()
        b = q.popleft()
        # print("solve", a, operator, b)
        if b == "(":
            b = solve_parenthesis()
            q.popleft()
        return a+b+operator

    while q:
        now = q.popleft()
        if now in "+-":
            operator_stack.append(now)
            continue
        elif now in "*/":
            make_postfix(now)
            continue
        elif now == "(":
            now = solve_parenthesis()
                
        if not num_stack:
            num_stack.append(now)
            continue
        
        # 다 지나왔다면 건너편 확인
        while q:
            next = q.popleft()
            if next in "*/":
                num_stack.append(now)
                make_postfix(next)
                now = num_stack.pop()
            else:
                q.appendleft(next)
                break
            
        num_stack.append(num_stack.pop()+now+operator_stack.pop())
        
        
    print(num_stack[0])
    
