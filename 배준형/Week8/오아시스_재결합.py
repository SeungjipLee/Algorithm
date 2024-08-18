# N 명이 서 있고
# 서로 마주 볼 수 있는 쌍의 수를 구하라

# 두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.

# 2 4 1 2 2 5 1
# 2 | 4
# 4 | 1 2 2 5 
# 5 | 1 

# 6 5 4 4 5 6  숫자가 내려가면 스택에 넣는다?

# 6 | 5 5 6 완전
# 5 | 4 4 5 6 불완전
# 불완전은 해소시켜줘야한다
# 4 4 5
# 4 5
# 5 6
# 5| 5(10) 6

# 6 | 5 5 6
# 5 | 4 4 5 6
# 4 | 4 5
# 4 | 5
# 5 | 6            11

# 스택에 시작하는 숫자와 마주볼 수 있는 숫자를 넣는다
# 마주보는 숫자가 자신보다 크면 더 이상 마주볼 수 있는 수는 없으므로 
# 스택에서 제거하고 쌍의 갯수를 최종 결과값에 더한다
# 
# 5가 50만개 있다고 생각해보셈
# 그러면 모두 서로를 바라볼 수 있음 이거 스택에 50만개 넣고 50만개 업데이트해야함

# 모든 쌍을 조사해야 하는가?
# 자기보다 작은 사람이 몇 사람인지 저장
# 자기보다 큰 사람이 몇 사람인지 저장

# 순서대로 스택에 넣는다.
# 자기보다 작은 친구를 스택에서 제거하면서 결과값에 더하기
# 같으면 갯수 늘리고 다시 스택에 넣기 

import sys
input_ = sys.stdin.readline

N = int(input_())
stack = [[0, 0] for _ in range(N)]

answer = 0
top = -1
end = -1

for _ in range(N):
    num = int(input_())
    print(num, stack, answer, top)
    if top == -1:
        top += 1
        stack[top] = [num, 1]
        continue
    if num < stack[top][0]:
        answer += 1
        top += 1
        stack[top] = [num, 1]
        continue
    # 들어오는 값이 top 보다 크거나 같다면
    tmp = 0
    cur = top
    flag = False
    while cur > -1:
        if stack[cur][0] == num:
            tmp += stack[cur][1]
            stack[cur][1] += 1
            flag = True
            cur -= 1
        elif stack[cur][0] < num:
            tmp += stack[cur][1]
            top -= 1
            cur -= 1
        else:
            tmp += 1
            break
    
    if not flag:
        top += 1
        stack[top] = [num, 1]
    answer += tmp
        
# print(stack)
print(answer)