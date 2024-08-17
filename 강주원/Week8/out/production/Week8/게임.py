x, y = map(int, input().split())
z = int(y*100/x)

ls = []
start, end = 0, x
while start <= end:
    mid = (start+end) // 2
    new_x, new_y = x + mid, y + mid
    win_rate = int(new_y*100/new_x)
    if win_rate == z:
        start = mid + 1
    else:
        ls.append(mid)
        end = mid - 1

if ls:
    print(min(ls))
else:
    print(-1)