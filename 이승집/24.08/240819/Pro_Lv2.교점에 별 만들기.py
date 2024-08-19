from itertools import combinations

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]


def get_cross(A, B):
    a, b, c = A
    d, e, f = B
    try:
        x = (b * f - c * e) / (a * e - d * b)
        y = (a * f - c * d) / (b * d - a * e)
    except ZeroDivisionError:
        return
    if int(x) == x and int(y) == y:
        return int(x), int(y)


ans = []

for i in combinations(line, 2):
    A = get_cross(i[0], i[1])
    if A:
        ans.append(A)

print(ans)

width_left = min(ans, key= lambda x: x[0])[0]
width_right = max(ans, key= lambda x: x[0])[0]
height_down = min(ans, key= lambda x: x[1])[1]
height_up = max(ans, key= lambda x: x[1])[1]

print(width_left, width_right, height_down, height_up)
width = width_right - width_left + 1
height = height_up - height_down + 1

answer = [['.']*width for _ in range(height)]

for dot in ans:
    answer[height_up- dot[1]][dot[0] - width_left] = "*"

answer = ["".join(i) for i in answer]

print(answer)
