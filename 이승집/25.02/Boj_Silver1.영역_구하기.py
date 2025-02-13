def main():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                board[j][i] = 1

    ans = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                continue

            cnt = 0
            stack = [(i, j)]
            board[i][j] = 1

            while stack:
                now_i, now_j = stack.pop()
                cnt += 1

                for k in range(4):
                    nxt_i = now_i + dx[k]
                    nxt_j = now_j + dy[k]

                    if (0 <= nxt_i < n) and (0 <= nxt_j < m) and (board[nxt_i][nxt_j] == 0):
                        board[nxt_i][nxt_j] = 1
                        stack.append((nxt_i, nxt_j))

            ans.append(cnt)


    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()

"""input
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""