n, l, w, h = map(int, input().split())

start, end = 0, max(l, w, h)
for i in range(100):
    mid = (start + end) / 2
    if (l // mid) * (w // mid) * (h // mid) >= n:
        start = mid
    else:
        end = mid

print(end)