import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = 0

arr = []
for i in scoville:
    heapq.heappush(arr, i)

while arr[0] < K:
    low = heapq.heappop(arr)
    try:
        next = heapq.heappop(arr)
    except IndexError:
        answer = -1
        break
    heapq.heappush(arr, low + 2 * next)
    answer += 1

print(answer)

