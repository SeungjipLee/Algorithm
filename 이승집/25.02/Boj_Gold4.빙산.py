import sys


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = 0


    def check_board():
        cnt = 0
        visited = [[0] * m for _ in range(n)]
        stack = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    continue

                if visited[i][j] == 1:
                    continue

                stack.append((i, j))
                visited[i][j] = 1

                while stack:
                    now_x, now_y = stack.pop()
                    for k in range(4):
                        next_x = now_x + dx[k]
                        next_y = now_y + dy[k]
                        if (0 <= next_x < n) and (0 <= next_y < m) and board[next_x][next_y] != 0 and visited[next_x][next_y] == 0:
                            stack.append((next_x, next_y))
                            visited[next_x][next_y] = 1
                cnt += 1
        return cnt


    def melt():
        do = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    continue
                mid = 0
                for k in range(4):
                    nxt_i = i + dx[k]
                    nxt_j = j + dy[k]
                    if (0 <= nxt_i < n) and (0 <= nxt_j < m) and (board[nxt_i][nxt_j] == 0):
                        mid += 1
                do.append((i, j, mid))

        for s, t, u in do:
            board[s][t] = max(0, board[s][t] - u)


    while True:
        c = check_board()
        if c > 1:
            print(answer)
            break
        elif c == 0:
            print(0)
            break
        else:
            melt()
        answer += 1


if __name__ == "__main__":
    main()

"""input
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""