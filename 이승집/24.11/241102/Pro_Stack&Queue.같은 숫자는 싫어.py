def solution(arr):
    stack = []
    for i in arr:
        if stack and stack[-1] == i:
            pass
        else:
            stack.append(i)
    return stack