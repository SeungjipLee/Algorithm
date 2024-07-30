n, m = map(int, input().split())
ls = list(map(int, input().split()))

start, end = max(ls), sum(ls)
check = end / m

while start <= end:
    mid = (start+end) // 2
    if check > end or check < start:
        break
    total, cnt = 0, 1
    for i in ls:
        if i + total > mid:
            total = 0
            cnt += 1
        total += i

    if cnt <= m:
        res = mid
        end = mid-1
    else:
        start = mid+1

print(res)