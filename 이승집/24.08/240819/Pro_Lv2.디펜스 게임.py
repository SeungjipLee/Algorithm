import heapq

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

Q = []
answer = 0

for i in range(len(enemy)):
    heapq.heappush(Q, -enemy[i])
    n -= enemy[i]

    if n < 0:
        if k > 0:
            n += -heapq.heappop(Q)
            k -= 1
        else:
            answer = i
            break

if answer == 0:
    answer = len(enemy)

print(answer)