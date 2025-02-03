def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ready = 0  # 익기 시작할 토마토 개수
    tomatos = []  # 익은 토마토 위치
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                ready += 1
            elif board[i][j] == 1:
                tomatos.append((i, j, 0))
    # 만약 변할 토마토가 없다면 0을 출력
    if ready == 0:
        print(0)
        return

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    ans = 0

    Q = deque(tomatos)
    while Q:
        now_x, now_y, turn = Q.popleft()
        ans = max(ans, turn)
        for k in range(4):
            new_x = now_x + dx[k]
            new_y = now_y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m and board[new_x][new_y] == 0:
                board[new_x][new_y] = turn + 1
                Q.append((new_x, new_y, turn + 1))
                ready -= 1

    if ready != 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
