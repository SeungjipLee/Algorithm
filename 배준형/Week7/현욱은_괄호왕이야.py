import sys
input_ = sys.stdin.readline

N = int(input_())
arr = list(input_())
matched = [0] * N
answer = []
stack = []

for i in range(N):
    now = arr[i]
    if now == "(":
        stack.append([now, i])
    else:
        if stack and stack[-1][0] == "(":
            pre, idx = stack.pop()
            matched[i] = 1
            matched[idx] = 1

result = 0
tmp = 0
for item in matched:
    if item == 0:
        tmp = 0
    tmp += item
    result = max(result, tmp)

print(result)