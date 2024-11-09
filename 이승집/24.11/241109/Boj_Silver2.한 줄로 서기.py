n = int(input())
arr = list(map(int, input().split()))

answer = [0] * n
for i in range(1, n + 1):
    mid = arr[i-1]
    for j in range(n):
        if mid == 0 and answer[j] == 0:
            answer[j] = i
            break

        if answer[j] <= 0:
            mid -= 1

for a in answer:
    print(a, end=" ")
