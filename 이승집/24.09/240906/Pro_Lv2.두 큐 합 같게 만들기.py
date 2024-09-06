from collections import deque

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

whole = sum(queue1) + sum(queue2)
answer = 0
N = len(queue1) + len(queue2)

if whole % 2:
    answer = -1
else:
    half = whole // 2
    Q1 = deque(queue1)
    Q2 = deque(queue2)
    start = sum(Q1)
    while start != half:
        if answer > 2 * N:
            answer = -1
            break

        if start < half:
            mid = Q2.popleft()
            start += mid
            Q1.append(mid)

        else:
            mid = Q1.popleft()
            start -= mid
            Q2.append(mid)

        answer += 1

print(answer)