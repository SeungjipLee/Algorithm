numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
answer = ""

now_left = 10
now_right = 12

cartesian = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    10: (3, 0), 0: (3, 1), 12: (3, 2)
}


def get_distance(i, j):
    (a, b) = cartesian[i]
    (c, d) = cartesian[j]
    return abs(a - c) + abs(b - d)


for i in numbers:
    if i in [1, 4, 7]:
        answer += "L"
        now_left = i
    elif i in [3, 6, 9]:
        answer += "R"
        now_right = i
    else:
        left_distance = get_distance(i, now_left)
        right_distance = get_distance(i, now_right)
        if left_distance < right_distance:
            answer += "L"
            now_left = i
        elif left_distance > right_distance:
            answer += "R"
            now_right = i
        else:
            if hand == "right":
                answer += "R"
                now_right = i
            else:
                answer += "L"
                now_left = i

print(answer)
print("LRLLRRLLLRR")