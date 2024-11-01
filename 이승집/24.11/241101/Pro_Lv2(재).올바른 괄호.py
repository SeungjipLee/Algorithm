def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
