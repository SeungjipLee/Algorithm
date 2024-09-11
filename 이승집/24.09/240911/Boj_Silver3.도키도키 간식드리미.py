from collections import deque

N = int(input())

nums = deque(list(map(int, input().split())))

hold = []
target = 1
answer = "Nice"

while nums or hold:
    if nums and nums[0] == target:  # 트럭에서 바로 목표 간식을 받을 수 있는 경우
        nums.popleft()
        target += 1
    elif hold and hold[-1] == target:  # 보조 스택에서 목표 간식을 받을 수 있는 경우
        hold.pop()
        target += 1
    elif nums:  # 위 두 경우가 아니라면 트럭에서 간식을 보조 스택에 넣는다
        hold.append(nums.popleft())
    else:  # 받을 수 있는 간식이 없으면 실패
        answer = "Sad"
        break

print(answer)
