from collections import deque

n, k = map(int, input().split())

# 방문 여부를 기록하는 리스트
visited = [False] * 100001
Q = deque([(n, 0)])
visited[n] = True

while Q:
    now, value = Q.popleft()

    if now == k:
        print(value)
        break

    for next_pos in (now - 1, now + 1, now * 2):
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = True
            Q.append((next_pos, value + 1))
