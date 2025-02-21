import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = []
purifiers = []  # 공기청정기 위치 (행)
for i in range(R):
    row = list(map(int, input().split()))
    room.append(row)
    if row[0] == -1:
        purifiers.append(i)

# 위쪽 공기청정기와 아래쪽 공기청정기 위치
upper = purifiers[0]
lower = purifiers[1]

# 미세먼지 확산을 위한 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread():
    """미세먼지 확산을 시뮬레이션하는 함수"""
    global room
    new_room = [[0] * C for _ in range(R)]
    # 공기청정기 위치는 그대로 -1로 유지
    new_room[upper][0] = -1
    new_room[lower][0] = -1

    for i in range(R):
        for j in range(C):
            # 미세먼지가 있는 칸이면
            if room[i][j] > 0:
                dust = room[i][j]
                spread_amount = dust // 5
                count = 0
                # 4방향으로 확산
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        new_room[ni][nj] += spread_amount
                        count += 1
                new_room[i][j] += dust - spread_amount * count
    room = new_room

def clean():
    """공기청정기 작동 (먼지 이동) 시뮬레이션 함수"""
    global room
    # --- 위쪽 공기청정기 (반시계방향) ---
    # 1. 위쪽 벽을 따라 왼쪽 열을 위로 당김
    for i in range(upper - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    room[0][0] = 0

    # 2. 위쪽 행을 왼쪽에서 오른쪽으로 당김
    for j in range(0, C - 1):
        room[0][j] = room[0][j + 1]
    room[0][C - 1] = 0

    # 3. 오른쪽 열을 위에서 아래로 당김
    for i in range(0, upper):
        room[i][C - 1] = room[i + 1][C - 1]
    room[upper][C - 1] = 0

    # 4. 공기청정기 행을 오른쪽에서 왼쪽으로 당김
    for j in range(C - 1, 1, -1):
        room[upper][j] = room[upper][j - 1]
    room[upper][1] = 0

    # --- 아래쪽 공기청정기 (시계방향) ---
    # 1. 왼쪽 열을 아래쪽 벽을 향해 당김
    for i in range(lower + 1, R - 1):
        room[i][0] = room[i + 1][0]
    room[R - 1][0] = 0

    # 2. 아래쪽 행을 왼쪽에서 오른쪽으로 당김
    for j in range(0, C - 1):
        room[R - 1][j] = room[R - 1][j + 1]
    room[R - 1][C - 1] = 0

    # 3. 오른쪽 열을 아래에서 위로 당김
    for i in range(R - 1, lower, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    room[lower][C - 1] = 0

    # 4. 공기청정기 행을 오른쪽에서 왼쪽으로 당김
    for j in range(C - 1, 1, -1):
        room[lower][j] = room[lower][j - 1]
    room[lower][1] = 0

# T초 동안 시뮬레이션 실행
for _ in range(T):
    spread()
    clean()

# 남아있는 미세먼지의 총량 계산 (공기청정기 칸은 -1이므로 제외)
result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]

print(result)
