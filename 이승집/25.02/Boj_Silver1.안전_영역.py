def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_height = max(max(row) for row in board)
    for h in range(0, max_height + 1):
        visited = [[0] * n for _ in range(n)]
        Q = deque([])
        mid = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1 or board[i][j] <= h:
                    continue

                if board[i][j] > h:
                    Q.append((i, j))
                    visited[i][j] = 1

                while Q:
                    now_x, now_y = Q.popleft()
                    for k in range(4):
                        nx = now_x + dx[k]
                        ny = now_y + dy[k]
                        if 0 <= nx < n  and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] > h:
                            Q.append((nx, ny))
                            visited[nx][ny] = 1

                mid += 1
        ans = max(ans, mid)
    print(ans)


if __name__ == "__main__":
    main()