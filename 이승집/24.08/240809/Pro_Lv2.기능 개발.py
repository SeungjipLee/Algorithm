from math import ceil

progresses = [40, 20, 30, 20]
speeds = [1, 1, 1, 1]
answer = []
l = len(progresses)
plan = [0] * l
for i in range(l):
    plan[i] = ceil((100 - progresses[i])/speeds[i])

print(plan)
mid = 0
cnt = 1

for i in range(l-1):
    if plan[i] > mid:
        mid = plan[i]
    if plan[i] < plan[i + 1] and plan[i + 1] > mid:
        answer.append(cnt)
        cnt = 1
        mid = 0
    else:
        cnt += 1
answer.append(cnt)
print(answer)