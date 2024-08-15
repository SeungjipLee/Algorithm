# 직사각형을 만난다
# 현재 몇번째 직사각형을 만났는지 정보를 저장한다
# ex 높이가 3이다
# 3: 1 이라는 정보를 스택에 담는다
# 스택의 top 을 보고 해당 높이보다 작으면 해당 높이까지 꺼내서 넓이를 계산한다
# 만약 스택이 비었다면 [현재높이, 이전 스택top의 시작위치] 를 저장한다
# 높이가 높다면 해당 높이까지 또 스택에 추가한다

import sys
input_ = sys.stdin.readline

N = int(input_())
stack = []
max_area = 0

for i in range(N):
    # print(stack)
    now = int(input_())
    if stack:
        height, started = stack[-1]
        if height == now:
            continue
        elif height < now:
            stack.append([now, i])
        else:
            while stack and stack[-1][0] > now:
                height, started = stack.pop()
                max_area = max(max_area, height * (i - started))
            if not stack or stack[-1][0] != now:
                stack.append([now, started])
    else:
        stack.append([now, i])
i += 1
while stack:
    height, started = stack.pop()
    max_area = max(max_area, height * (i - started))
print(max_area)