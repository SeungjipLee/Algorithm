import sys
from collections import deque


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    answer = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(a, b):
        visited = [[0] * m for _ in range(n)]
        visited[a][b] = 1
        Q = deque([(a, b, 0)])
        mid = 0

        while Q:
            now_x, now_y, val = Q.popleft()
            mid = max(val, mid)
            for k in range(4):
                nxt_x = now_x + dx[k]
                nxt_y = now_y + dy[k]
                if 0 <= nxt_x < n and 0 <= nxt_y < m and board[nxt_x][nxt_y] == "L" and visited[nxt_x][nxt_y] == 0:
                    Q.append((nxt_x, nxt_y, val + 1))
                    visited[nxt_x][nxt_y] = 1

        return mid


    for i in range(n):
        for j in range(m):
            if board[i][j] == "L":
                answer = max(answer, bfs(i, j))

    print(answer)


if __name__ == "__main__":
    main()

"""input
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""