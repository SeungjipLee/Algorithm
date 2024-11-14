arr = [[]] + [list(map(int, input())) for _ in range(4)]
k = int(input())
do = [tuple(map(int, input().split())) for _ in range(k)]


# 반시계
def roll_left(L):
    mid = L.pop(0)
    L.append(mid)

# 시계
def roll_right(R):
    mid = R.pop()
    R.insert(0, mid)

def rotate_gears(idx, direction):
    directions = [0] * 5
    directions[idx] = direction

    for i in range(idx, 4):
        if arr[i][2] != arr[i + 1][6]:
            directions[i + 1] = -directions[i]
        else:
            break

    for i in range(idx, 1, -1):
        if arr[i][6] != arr[i - 1][2]:
            directions[i - 1] = -directions[i]
        else:
            break

    for i in range(1, 5):
        if directions[i] == 1:
            roll_right(arr[i])
        elif directions[i] == -1:
            roll_left(arr[i])


for rot in do:
    idx, dir = rot
    rotate_gears(idx, dir)

answer = 0

for i in range(1, 5):
    if arr[i][0] == 1:
        answer += 2 ** (i - 1)

print(answer)