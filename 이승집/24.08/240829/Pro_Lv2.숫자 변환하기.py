from collections import deque

x, y, n = 2, 17, 3

Q = deque([(x, 0)])
visited = {x}
answer = -1
while Q:
    now, value = Q.popleft()
    next_values = [now + n, now * 2, now * 3]

    for next_value in next_values:
        if next_value == y:
            answer = value + 1
            break
        if next_value < y and next_value not in visited:
            visited.add(next_value)
            Q.append((next_value, value + 1))

print(answer)