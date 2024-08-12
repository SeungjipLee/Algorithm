from pprint import pprint

n = 5

Board = [[0] * (i + 1) for i in range(n)]
Board[0][0] = 1

"""
동작은 크게 3개

1. 아래로 내리기
2. 오른쪽으로 밀기
3. 위로 올리기

"""
# 0은 아래로, 1은 오른쪽 2는 위로
mod = 0

dx = [1, 0, -1]
dy = [0, 1, -1]

i = j = 0
cnt = 0
value = 2
while cnt != n * (n + 1) // 2 + n:
    if 0 <= i + dx[mod] < n and 0 <= j + dy[mod] < n and Board[i + dx[mod]][j + dy[mod]] == 0:
        i += dx[mod]
        j += dy[mod]
        Board[i][j] = value
        value += 1
    else:
        mod = (mod + 1)%3

    cnt += 1
pprint(Board)
answer = []
for i in Board:
    for j in i:
        answer.append(j)
pprint(answer)
