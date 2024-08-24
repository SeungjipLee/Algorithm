land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

def solution(land):
    # 각 행을 순회하며
    for i in range(1, len(land)):
        # 현재 행의 각 열에 대해 최대값을 계산
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])


print(solution(land))