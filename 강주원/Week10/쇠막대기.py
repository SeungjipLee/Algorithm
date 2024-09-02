import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
res = 0
for i in s:
    if i == '(':
        stack.append(i)
        is_laser = 1
    else:
        stack.pop()
        if is_laser == 1:
            res += len(stack)
        else:
            res += 1
        is_laser = 0

print(res)