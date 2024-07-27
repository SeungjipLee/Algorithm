n = 4

Board = [[0] * n for _ in range(n)]
Board[0][0] = 1

# (0, 0) 좌표부터 시작해서 이동한다
# 이동 규칙은 오른쪽으로 가다가 막히면 아래
# 아래로 가다가 막히면 왼쪽
# 왼쪽 가다가 막히면 위로
# 위로 가다가 막히면 오른쪽으로 간다
# 델타 탐색을 써야겠네

# 델타 탐색(우하좌상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 방향, 위치, 값
now_direction = 0
now_i = 0
now_j = 0
now_value = 2

while now_value <= n ** 2:
    # 방향으로 한 번 가보자
    new_i = now_i + dx[now_direction]
    new_j = now_j + dy[now_direction]

    # 만약 튀어나온다면 꺾어야한다.
    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
        now_direction = (now_direction + 1) % 4
        continue
    # 0이 아닌 값이 들어있다면?
    elif Board[new_i][new_j] != 0:
        now_direction = (now_direction + 1) % 4
        continue
    # 정상 범위에 0을 만난다면 올바르게 온 것
    else:
        Board[new_i][new_j] = now_value
        now_value += 1
        now_i = new_i
        now_j = new_j

print(Board)