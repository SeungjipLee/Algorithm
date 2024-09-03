lane = input()

answer = 0
stack = ["("]

for i in range(1, len(lane)):
    if lane[i] == "(":
        stack.append("(")
    else:
        if lane[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1


print(answer)