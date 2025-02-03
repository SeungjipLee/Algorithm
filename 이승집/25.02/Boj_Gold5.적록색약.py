def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    board = [list(input().strip()) for _ in range(n)]

    normal = 0
    abnormal = 0

    visited_normal = [[0] * n for _ in range(n)]
    visited_abnormal = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 정상인 카운팅
    for i in range(n):
        for j in range(n):
            # 만약 방문했다면 넘어가자
            if visited_normal[i][j] == 1:
                continue

            current_color = board[i][j]
            Q_normal = deque([(i, j)])
            visited_normal[i][j] = 1
            while Q_normal:
                now_x, now_y = Q_normal.popleft()
                for k in range(4):
                    next_x = now_x + dx[k]
                    next_y = now_y + dy[k]
                    if 0 <= next_x < n and 0 <= next_y < n and visited_normal[next_x][next_y] == 0 and board[next_x][next_y] == current_color:
                        Q_normal.append((next_x, next_y))
                        visited_normal[next_x][next_y] = 1
            normal += 1
    # 비정상인 카운팅
    for i in range(n):
        for j in range(n):
            # 만약 방문했다면 넘어가자
            if visited_abnormal[i][j] == 1:
                continue

            current_color = board[i][j]
            if current_color in "RG":
                current_color = "RG"
            Q_abnormal = deque([(i, j)])
            visited_abnormal[i][j] = 1
            while Q_abnormal:
                now_x, now_y = Q_abnormal.popleft()
                for k in range(4):
                    next_x = now_x + dx[k]
                    next_y = now_y + dy[k]
                    if 0 <= next_x < n and 0 <= next_y < n and visited_abnormal[next_x][next_y] == 0 and \
                            board[next_x][next_y] in current_color:
                        Q_abnormal.append((next_x, next_y))
                        visited_abnormal[next_x][next_y] = 1
            abnormal += 1

    print(normal, abnormal)

if __name__ == "__main__":
    main()
