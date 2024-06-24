from collections import deque
s = input()
es = input()
stack = []
temp = deque([])
length = len(es)

for st in s:
    if len(temp) == length:
        if ''.join(temp) == es:
            temp = deque([])
            if stack and len(temp) != length:
                while stack and len(temp) != length-1:
                    temp.appendleft(stack.pop())

        else:
            stack.append(temp.popleft())

    temp.append(st)

if ''.join(temp) == es:
    temp = deque([])

if not temp and not stack:
    res = 'FRULA'
else:
    res = ''.join(stack) + ''.join(temp)

print(res)


# 더 나은 풀이
'''
import sys
input = sys.stdin.readline

n = input().strip()
a = input().strip()
aa = list(a)
len_a = len(a)
last_a = a[-1]

stack = []
for i in range(len(n)):
    stack.append(n[i])
    if n[i] == last_a and stack[-len_a:] == aa:
        del stack[-len_a:]

if stack:
    print(''.join(stack))    
else:
    print("FRULA")
'''