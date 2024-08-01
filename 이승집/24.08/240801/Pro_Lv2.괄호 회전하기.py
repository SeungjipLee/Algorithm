s = "}]()[{"
n = len(s)
answer = 0

for push in range(n):
    stack = []
    flag = True
    for i in range(n):
        k = s[(i + push)%n]
        if k in "([{":
            stack.append(k)
        elif k == ")" and stack and stack[-1]=="(":
            stack.pop()
        elif k == "}" and stack and stack[-1]=="{":
            stack.pop()
        elif k == "]" and stack and stack[-1]=="[":
            stack.pop()
        else:
            flag = False
            break

    if not stack and flag:
        answer += 1

print(answer)