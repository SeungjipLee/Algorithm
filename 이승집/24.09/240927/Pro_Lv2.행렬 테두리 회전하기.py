from collections import deque

rows = 6
cols = 6

queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

boards = [[0] * (cols + 1) for _ in range(rows + 1)]
value = 1
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        boards[i][j] = value
        value += 1

print(boards)


for query in queries:
    si, sj, ei, ej = query
    ni, nj = si, sj
    k = 0
    save = deque([boards[si][sj]])
    minimum = boards[si][sj]
    while nj < ej:
        nj += 1
        save.append(boards[ni][nj])
        out = save.popleft()
        if out < minimum:
            minimum = out
        boards[ni][nj] = out
        print(save)

    while ni < ei:
        ni += 1
        save.append(boards[ni][nj])
        out = save.popleft()
        if out < minimum:
            minimum = out
        boards[ni][nj] = out
        print(save)

    while nj > sj:
        nj -= 1
        save.append(boards[ni][nj])
        out = save.popleft()
        if out < minimum:
            minimum = out
        boards[ni][nj] = out
        print(save)

    while ni > si:
        ni -= 1
        save.append(boards[ni][nj])
        out = save.popleft()
        if out < minimum:
            minimum = out
        boards[ni][nj] = out
        print(save)

    print(minimum)
