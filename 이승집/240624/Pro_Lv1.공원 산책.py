park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]

# 2차원 배열 만들어 두고
Board = [[0] * len(park[0]) for _ in range(len(park))]

# 현재 위치 잡고
now_i = 0
now_j = 0

# 2차원 배열에 넣자
for i in range(len(park)):
    for j in range(len(park[i])):
        Board[i][j] = park[i][j]
        if park[i][j] == "S":
            # 현재 위치는 출발점으로
            now_i, now_j = i, j

# 방향도 미리 세팅해두자
gogo = {"W": [0, -1], "E": [0, 1], "N": [-1, 0], "S": [1, 0]}


# 명령 시행하자
for k in routes:
    direction, amount = k.split()
    flag = True
    temp_i = 0
    temp_j = 0

    for l in range(int(amount)):
        new_i = now_i + gogo[direction][0] * (l + 1)
        new_j = now_j + gogo[direction][1] * (l + 1)

        # 튀어 나간다면 안 가
        if new_i < 0 or new_i >= len(park) or new_j < 0 or new_j >= len(park[0]):
            flag = False
            break

        # 장애물 있어도 안 가
        elif Board[new_i][new_j] == "X":
            flag = False
            break

        # 올 클
        else:
            temp_i = new_i
            temp_j = new_j

    if flag:
        now_i = temp_i
        now_j = temp_j


print(now_i, now_j)