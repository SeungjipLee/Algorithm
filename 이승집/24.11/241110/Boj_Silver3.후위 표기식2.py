n = int(input())

arr = list(input())
value = dict()

for i in range(n):
    A = int(input())
    value[chr(65 + i)] = A

stack = []


def cal(a, b, s):
    if s == "+":
        return a + b
    elif s == "-":
        return a - b
    elif s == "/":
        return a / b
    else:
        return a * b


for i in arr:
    if i in "+-*/":
        a = stack.pop()
        b = stack.pop()
        stack.append(cal(b, a, i))
    else:
        stack.append(value[i])

print(f'{stack[0]:.2f}')
