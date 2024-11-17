N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = max(map(max, board))
answer = 0

visited = [[False] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 가지치기: 현재 합에 최대값을 더해도 answer보다 작으면 탐색 중단
            if total + max_value * (4 - depth) <= answer:
                continue
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False


def check_t_shape(x, y):
    global answer
    center = board[x][y]
    for i in range(4):
        temp = center
        valid = True
        for j in range(3):
            idx = (i + j) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M):
                valid = False
                break
            temp += board[nx][ny]
        if valid:
            answer = max(answer, temp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_t_shape(i, j)

print(answer)
