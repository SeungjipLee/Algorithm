import sys

def main():
    input = sys.stdin.readline
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(minimum, maximum):
        change_flag = False
        visited = [[0] * n for _ in range(n)]
        stack = []
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    stack.append((i, j, board[i][j]))
                    visited[i][j] = 1

                mid = board[i][j]
                store = [(i, j)]
                while stack:
                    now_x, now_y, val = stack.pop()
                    for k in range(4):
                        next_x = now_x + dx[k]
                        next_y = now_y + dy[k]
                        if (0 <= next_x < n) and (0 <= next_y < n) and (visited[next_x][next_y] == 0) and (minimum <= abs(val - board[next_x][next_y]) <= maximum):
                            stack.append((next_x, next_y, board[next_x][next_y]))
                            visited[next_x][next_y] = 1
                            mid += board[next_x][next_y]
                            store.append((next_x, next_y))
                            change_flag = True

                avg = mid // len(store)
                for p, q in store:
                    board[p][q] = avg

        return change_flag

    while True:
        if dfs(l, r):
            answer += 1
        else:
            break

    print(answer)


if __name__ == "__main__":
    main()

"""input
3 5 10
10 15 20
20 30 25
40 22 10
"""