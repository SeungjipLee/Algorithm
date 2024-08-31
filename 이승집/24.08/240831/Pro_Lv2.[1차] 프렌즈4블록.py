m = n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def solution(m, n, board):
    # 보드를 리스트의 리스트로 변환
    board = [list(row) for row in board]
    print(board)
    answer = 0

    while True:
        mid = set()
        # 2x2 블록 검사
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "*":
                    continue
                current = board[i][j]
                if current == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    mid.add((i, j))
                    mid.add((i + 1, j))
                    mid.add((i, j + 1))
                    mid.add((i + 1, j + 1))

        # 제거할 블록이 없으면 종료
        if not mid:
            break

        # 블록 제거 및 카운트
        answer += len(mid)
        for (i, j) in mid:
            board[i][j] = "*"

        # 블록 내리기
        for j in range(n):
            empty = [board[i][j] for i in range(m) if board[i][j] != "*"]
            print(empty)
            for i in range(m - 1, -1, -1):
                if empty:
                    board[i][j] = empty.pop()
                else:
                    board[i][j] = "*"

    return answer

print(solution(m, n, board))