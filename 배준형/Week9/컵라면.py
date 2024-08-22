import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
arr = [list(minput()) for _ in range(N)]
arr.sort(key=lambda x: x[0])
h = []

day = N+1
cnt = 0
i = N-1
answer = 0
while True:
    day -= 1
    if day == 0:
        break

    while i >= 0 and arr[i][0] == day:
        heapq.heappush(h, -arr[i][1])
        i -= 1

    if h:
        val = heapq.heappop(h)
        answer += -val 
        cnt += 1

print(answer)