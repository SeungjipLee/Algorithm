answer = ''

def main():
    global answer
    import sys
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip())for _ in range(n)]


    def check(length, idx1, idx2):
        global answer
        if length == 1:
            answer += board[idx1][idx2]
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
            answer += standard
        else:
            m = length//2
            answer += "("
            check(m, idx1, idx2)
            check(m, idx1, idx2 + m)
            check(m, idx1 + m, idx2)
            check(m, idx1 + m, idx2 + m)
            answer += ")"

    check(n, 0, 0)

    print(answer)


if __name__ == '__main__':
    main()

"""input
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
"""