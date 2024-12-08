# 방향 벡터 설정: 상, 우, 하, 좌
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 블록 반사 설정
block_reflect = {
    1: [2, 3, 1, 0],
    2: [1, 3, 0, 2],
    3: [3, 2, 0, 1],
    4: [2, 0, 3, 1],
    5: [2, 3, 0, 1]
}


def simulate(board, start_x, start_y, start_dir, wormholes):
    x, y, d = start_x, start_y, start_dir
    score = 0
    n = len(board)

    while True:
        x += directions[d][0]
        y += directions[d][1]

        # 벽에 부딪힌 경우
        if x < 0 or x >= n or y < 0 or y >= n:
            d = (d + 2) % 4  # 방향 반전
            score += 1
            continue

        cell = board[x][y]

        # 블랙홀에 도달하거나 시작 위치로 돌아온 경우
        if cell == -1 or (x == start_x and y == start_y):
            return score

        # 블록에 부딪힌 경우
        if 1 <= cell <= 5:
            d = block_reflect[cell][d]
            score += 1

        # 웜홀에 도달한 경우
        elif 6 <= cell <= 10:
            x, y = wormholes[(x, y)]


def find_wormholes(board):
    wormholes = {}
    wormhole_pairs = {}

    for i in range(len(board)):
        for j in range(len(board[i])):
            if 6 <= board[i][j] <= 10:
                num = board[i][j]
                if num not in wormhole_pairs:
                    wormhole_pairs[num] = [(i, j)]
                else:
                    wormhole_pairs[num].append((i, j))

    for num, positions in wormhole_pairs.items():
        if len(positions) == 2:
            wormholes[positions[0]] = positions[1]
            wormholes[positions[1]] = positions[0]

    return wormholes


def solve(board):
    n = len(board)
    max_score = 0
    wormholes = find_wormholes(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:  # 빈 공간에서 시작
                for d in range(4):  # 네 방향 시뮬레이션
                    score = simulate(board, i, j, d, wormholes)
                    max_score = max(max_score, score)

    return max_score


# 입력 처리 예시
t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = solve(board)
    print(f"#{test_case} {result}")
