wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]

lux = 51
rdx = -1
idx2 = -1
mid2 = []

for i in wallpaper:
    idx2 += 1
    if "#" not in i:
        continue
    mid2.append(idx2)
    mid = []
    idx = 0
    for j in i:
        if j == "#":
            mid.append(idx)
        idx += 1

    if min(mid) < lux:
        lux = min(mid)

    if max(mid) > rdx:
        rdx = max(mid)


print(lux, rdx + 1)
print(min(mid2), max(mid2) + 1)