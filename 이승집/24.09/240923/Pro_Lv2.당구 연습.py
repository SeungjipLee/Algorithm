m = 10
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]

answer = []


def check_four_side(point):
    global startX, startY
    x, y = point
    left = (-x, y)
    right = (2 * m - x, y)
    up = (x, 2 * n - y)
    down = (x, -y)
    for_check = [left, right, up, down]

    if (startX == x) and (startY > y):
        for_check.pop(3)
    elif (startX == x) and (startY < y):
        for_check.pop(2)
    elif (startY == y) and (startX > x):
        for_check.pop(0)
    elif (startY == y) and (startX < x):
        for_check.pop(1)

    return for_check


for ball in balls:
    mid = check_four_side(ball)
    minimum = m ** 2 + n ** 2 + 1
    for direction in mid:
        val = (startX - direction[0]) ** 2 + (startY - direction[1]) ** 2
        if val < minimum:
            minimum = val
        print((startX, startY), direction, val)

    print("---------")

    answer.append(minimum)

print(answer)
