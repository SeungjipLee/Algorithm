def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while True:
        print(board)
        num, board = board_game(m, n, board)
        if num == 0:
            break
        answer += num
        board = board_change(m, n, board)
        
    return answer

def board_game(n, m, board):
    result = 0
    visited = [[0] * m for _ in range(n)]
    arr = []
    for i in range(n-1):
        for j in range(m-1):
            target = board[i][j]
            if target == "-":
                continue
            for dx, dy in [[0, 1], [1, 0], [1, 1]]:
                nx, ny = i+dx, j+dy
                print(nx, ny)
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if board[nx][ny] != target or board[nx][ny] == "-":
                    break
            else:
                arr.append([i, j])
    for i, j in arr:
        for dx, dy in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            nx, ny = i+dx, j+dy
            if not visited[nx][ny]:
                result += 1
            visited[nx][ny] = 1
            board[nx][ny] = "-"

    return result, board
        

def board_change(n, m, board):
    for j in range(m):
        for i in range(n-1):
            if board[i][j] != "-" and board[i+1][j] == "-":
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    return board

solution(4, 5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])