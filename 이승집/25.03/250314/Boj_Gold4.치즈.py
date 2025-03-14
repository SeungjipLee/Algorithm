import sys
from collections import deque


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    def find_air():
        Q = deque([(0, 0)])
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        melt = []

        while Q:
            x, y = Q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
                    if board[nx][ny] == 0:
                        Q.append((nx, ny))
                    elif board[nx][ny] == 1:
                        melt.append((nx, ny))
                    visited[nx][ny] = 1

        return melt

    time = 0
    last_cheese = 0

    while True:
        melting_cheese = find_air()

        if not melting_cheese:
            print(time)
            print(last_cheese)
            break

        last_cheese = len(melting_cheese)

        for x, y in melting_cheese:
            board[x][y] = 0

        time += 1

if __name__ == "__main__":
    main()

"""input
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
"""