ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
answer = 0

stack = []
for i in ingredient:
    stack.append(i)
    if stack[-4:] == [1, 2, 3, 1]:
        for _ in range(4):
            stack.pop()
        answer += 1

print(answer)