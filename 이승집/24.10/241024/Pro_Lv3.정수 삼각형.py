def solution(triangle):
    answer = 0
    N = len(triangle)

    for i in range(1, N):
        for j in range(i + 1):
            mid = []
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[N - 1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))