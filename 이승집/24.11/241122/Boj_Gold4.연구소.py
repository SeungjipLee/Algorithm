from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread_virus(grid, virus_locations):
    queue = deque(virus_locations)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                queue.append((nx, ny))


def get_safe_area(grid):
    return sum(row.count(0) for row in grid)


empty_spaces = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]
virus_locations = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]

max_safe_area = 0

for walls in combinations(empty_spaces, 3):
    temp_grid = copy.deepcopy(grid)

    for x, y in walls:
        temp_grid[x][y] = 1

    spread_virus(temp_grid, virus_locations)

    max_safe_area = max(max_safe_area, get_safe_area(temp_grid))

print(max_safe_area)
