N, K = map(int, input().split())

weights = list(map(int, input().split()))

weights.sort()
cnt = 0
start, end = 0, N - 1

while start < end:
    if weights[start] + weights[end] <= K:
        cnt += 1
        start += 1
        end -= 1
    else:
        end -= 1

print(cnt)
