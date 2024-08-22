numbers = [9, 1, 5, 3, 6, 2]
answer = [-1]

stack = [numbers[-1]]

for i in range(len(numbers)-2, -1, -1):
    while stack:
        if stack[-1] <= numbers[i]:
            stack.pop()
        else:
            answer.append(stack[-1])
            break
    if not stack:
        answer.append(-1)
    stack.append(numbers[i])
print(answer)