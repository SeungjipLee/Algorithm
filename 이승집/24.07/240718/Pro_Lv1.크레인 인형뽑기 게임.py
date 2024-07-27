board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
answer = 0
stack = []

# moves를 순회
for i in moves:
    # 뽑은 숫자는 가로로 움직이는 것
    for j in range(len(board[0])):
        if board[j][i - 1] != 0:
            stack.append(board[j][i - 1])
            board[j][i - 1] = 0
            break

    if len(stack) >= 2 and stack[-1] == stack[-2]:
        for _ in range(2):
            stack.pop()
        answer += 2

print(answer)
