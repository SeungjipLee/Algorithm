from collections import deque


def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def bfs(place, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    while queue:
        cx, cy, dist = queue.popleft()
        if dist > 0 and place[cx][cy] == 'P':
            return False
        if dist < 2:
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny) and not visited[nx][ny] and place[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return True


def check_place(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(place, i, j):
                    return 0
    return 1


def solution(places):
    return [check_place(place) for place in places]
