def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    m, n, h = map(int, input().split())
    board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    ready = 0
    tomatoes = deque([])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    ready += 1
                elif board[i][j][k] == 1:
                    tomatoes.append((i, j, k, 0))

    if ready == 0:
        print(0)
        return

    # 앞 우 뒤 좌 상 하
    dz = [0, 0, 0, 0, 1, -1]
    dy = [1, 0, -1, 0, 0, 0]
    dx = [0, 1, 0, -1, 0, 0]

    ans = 0

    while tomatoes:
        now_z, now_y, now_x, turn = tomatoes.popleft()
        ans = max(ans, turn)
        for k in range(6):
            nxt_z = now_z + dz[k]
            nxt_y = now_y + dy[k]
            nxt_x = now_x + dx[k]
            if 0 <= nxt_z < h and 0 <= nxt_y < n and 0 <= nxt_x < m and board[nxt_z][nxt_y][nxt_x] == 0:
                board[nxt_z][nxt_y][nxt_x] = turn + 1
                tomatoes.append((nxt_z, nxt_y, nxt_x, turn + 1))
                ready -= 1

    if ready != 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()