N = int(input())
arr = list(map(int, input().split()))
B = int(input())
if sum(arr) <= B:
    print(max(arr))
    exit(0)
maxi = 0

start, end = 0, B

while start <= end:
    mid = (start + end) // 2
    acc = 0
    for money in arr:
        if money < mid:
            acc += money
        else:
            acc += mid
    if acc <= B:
        maxi = max(maxi, mid)
        start = mid + 1
    else:
        end = mid - 1

print(maxi)