import heapq


def solution(board):
    N = len(board)
    minimum = [[[int(1e9)] * 4 for _ in range(N)] for _ in range(N)]
    for i in range(4):
        minimum[0][0][i] = 0

    # 비용, x좌표, y좌표, 마지막 온 방향
    Q = [(0, 0, 0, -1)]

    # 0 = 우, 1 = 하, 2 = 좌, 3 = 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while Q:
        now_c, now_x, now_y, last_dir = heapq.heappop(Q)
        for k in range(4):
            next_x = now_x + dx[k]
            next_y = now_y + dy[k]

            if 0 > next_x or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if board[next_x][next_y] == 1:
                continue

            if last_dir == -1 or k == last_dir:
                next_cost = now_c + 100
            else:
                next_cost = now_c + 600

            if minimum[next_x][next_y][k] > next_cost:
                minimum[next_x][next_y][k] = next_cost
                heapq.heappush(Q, (next_cost, next_x, next_y, k))

    return min(minimum[N - 1][N - 1])


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

