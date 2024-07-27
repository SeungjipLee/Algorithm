s = "baabaa"
stack = []

for i in s:
    if stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)

if stack:
    print(0)
else:
    print(1)