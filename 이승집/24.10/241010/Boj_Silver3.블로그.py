import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:M])
maximum = current_sum
cnt = 1

for i in range(M, N):
    current_sum = current_sum - arr[i - M] + arr[i]
    if current_sum > maximum:
        maximum = current_sum
        cnt = 1
    elif current_sum == maximum:
        cnt += 1

if maximum == 0:
    print("SAD")
else:
    print(maximum)
    print(cnt)