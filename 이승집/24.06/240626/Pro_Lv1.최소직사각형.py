sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

max1 = 0
max2 = 0

for i in sizes:
    i.sort()
    if i[0] > max1:
        max1 = i[0]
    if i[1] > max2:
        max2 = i[1]

print(max1, max2)