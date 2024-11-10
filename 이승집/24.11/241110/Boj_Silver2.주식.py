T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    max_so_far = 0
    for i in range(n - 1, -1, -1):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        answer += max_so_far - arr[i]

    print(answer)