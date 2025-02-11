
def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = [0, 0]


    def check(length, idx1, idx2):
        if length == 1:
            answer[board[idx1][idx2]] += 1
            return

        standard = board[idx1][idx2]
        flag = True

        for i in range(idx1, idx1 + length):
            for j in range(idx2, idx2 + length):
                if board[i][j] != standard:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            answer[standard] += 1
        else:
            m = length // 2
            check(m, idx1, idx2)
            check(m, idx1 + m, idx2)
            check(m, idx1, idx2 + m)
            check(m, idx1 + m, idx2 + m)

    check(n, 0, 0)

    for i in answer:
        print(i)

if __name__ == '__main__':
    main()


"""input
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""