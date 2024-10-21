from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

dq = deque([(i + 1, balloons[i]) for i in range(n)])

result = []

while dq:
    idx, num = dq.popleft()
    result.append(idx)

    if not dq:
        break

    if num > 0:
        dq.rotate(-(num - 1))
    else:
        dq.rotate(-num)

print(' '.join(map(str, result)))
