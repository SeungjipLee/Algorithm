def solution(ingredient):
    answer = 0
    n = len(ingredient)
    stack = []
    for ing in ingredient:
        # print(ing, stack)
        if stack:
            if ing == 1 and stack[-1] == (3, 2):
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
            elif ing == 2 and stack[-1] == (1, 0):
                stack.append((2, 1))
            elif ing == 3 and stack[-1] == (2, 1):
                stack.append((3, 2))
            else:
                stack.append((ing, 0))
        else:
            stack.append((ing, 0))
    return answer