s = "(())()"

stack = []
answer = True

for i in s:
    if i == "(":
        stack.append(i)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            answer = False
            break

if stack:
    answer = False
    
print(answer)