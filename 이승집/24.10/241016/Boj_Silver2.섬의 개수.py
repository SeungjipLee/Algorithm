import sys

sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def dfs(x, y, grid, visited, w, h):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny, grid, visited, w, h)


def count_islands(w, h, grid):
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited, w, h)
                count += 1

    return count


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]

    print(count_islands(w, h, grid))
