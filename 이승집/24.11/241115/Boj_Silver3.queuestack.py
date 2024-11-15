from collections import deque

n = int(input())
queue_or_stack = list(map(int, input().split()))
data = list(map(int, input().split()))
m = int(input())
extra_data = list(map(int, input().split()))

queue_data = deque(data[i] for i in range(n) if queue_or_stack[i] == 0)

result = []
for x in extra_data:
    if queue_data:
        result.append(queue_data.popleft())
    else:
        result.append(x)

print(" ".join(map(str, result)))
