from collections import deque

prices = [5, 1, 3, 1, 2]
N = len(prices)
answer = [-1] * N
mid = []

for i in range(N):
    mid.append((prices[i], i))

mid.sort()
mid = deque(mid)

while mid:
    now = mid.popleft()
    k = -1
    for j in range(now[1], N):
        if answer[j] == -1:
            k += 1
        else:
            k += 1
            break
    answer[now[1]] = k

