N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

move = [-1, 0, 1]

# stacking_min을 각 위치에서 이전 방향별 최소 비용을 저장하도록 변경
stacking_min = [[float('inf')] * 3 for _ in range(M)]

# 첫 번째 행 초기화
for j in range(M):
    for k in range(3):
        stacking_min[j][k] = board[0][j]

for i in range(1, N):
    arr = [[float('inf')] * 3 for _ in range(M)]
    for j in range(M):
        for dir_index, dir in enumerate(move):
            nj = j - dir  # 이전 위치
            if 0 <= nj < M:
                for prev_dir_index in range(3):
                    if dir_index == prev_dir_index:
                        continue  # 같은 방향 연속 이동 불가
                    cost = stacking_min[nj][prev_dir_index] + board[i][j]
                    if cost < arr[j][dir_index]:
                        arr[j][dir_index] = cost
    stacking_min = arr

# 마지막 행에서 최소 비용 찾기
result = min(min(stacking_min[j]) for j in range(M))
print(result)
