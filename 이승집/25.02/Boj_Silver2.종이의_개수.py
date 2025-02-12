def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = [0, 0, 0]

    def cnt(n, idx1, idx2):
        if n == 1:
            ans[board[idx1][idx2] + 1] += 1
            return

        standard = board[idx1][idx2]
        flag = True

        for i in range(idx1, idx1 + n):
            for j in range(idx2, idx2 + n):
                if board[i][j] != standard:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            ans[standard + 1] += 1
        else:
            d = n//3
            cnt(d, idx1, idx2)
            cnt(d, idx1, idx2 + d)
            cnt(d, idx1, idx2 + 2 * d)
            cnt(d, idx1 + d, idx2)
            cnt(d, idx1 + d, idx2 + d)
            cnt(d, idx1 + d, idx2 + 2 * d)
            cnt(d, idx1 + 2 * d, idx2)
            cnt(d, idx1 + 2 * d, idx2 + d)
            cnt(d, idx1 + 2 * d, idx2 + 2 * d)

    cnt(n, 0, 0)
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()


"""input
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""