from collections import deque
n = int(input())
cards = deque(list(map(int, input().split())))

i, cnt = 1, 0
while cards:
    x = cards.popleft()
    if x == i:
        i += 1
    else:
        cnt += 1

print(cnt)