from collections import deque

n, m = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

Q = deque([(1, 0)])
visited = [False] * 101

while Q:
    now, acc = Q.popleft()

    for i in range(1, 7):
        nxt = now + i
        if nxt > 100:
            continue

        if nxt in ladders:
            nxt = ladders[nxt]
        elif nxt in snakes:
            nxt = snakes[nxt]

        if nxt == 100:
            print(acc + 1)
            exit(0)

        if not visited[nxt]:
            visited[nxt] = True
            Q.append((nxt, acc + 1))