import sys
input_ = sys.stdin.readline

arr = list(input_().rstrip())
stack = []
answer = 0
pre = ""
for item in arr:
    if item == "(":
        stack.append(item)
        pre = "("
    else:
        stack.pop()  
        if pre == "(":
            answer += len(stack)
        else:
            answer += 1
        pre = ")"
print(answer)