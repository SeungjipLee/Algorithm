def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 열쇠를 90도 회전하는 함수
    def rotate(matrix):
        return [[matrix[M - j - 1][i] for j in range(M)] for i in range(M)]

    # 자물쇠를 확장하는 함수
    def get_expanded_lock():
        size = N + 2 * M
        expanded_lock = [[0] * size for _ in range(size)]
        for i in range(N):
            for j in range(N):
                expanded_lock[i + M][j + M] = lock[i][j]
        return expanded_lock

    # 자물쇠가 열리는지 확인하는 함수
    def check(x, y, key, expanded_lock):
        size = N + 2 * M
        temp_lock = [row[:] for row in expanded_lock]  # 깊은 복사
        # 열쇠를 자물쇠에 더함
        for i in range(M):
            for j in range(M):
                temp_lock[x + i][y + j] += key[i][j]
        # 자물쇠 영역이 모두 1인지 확인
        for i in range(N):
            for j in range(N):
                if temp_lock[M + i][M + j] != 1:
                    return False
        return True

    expanded_lock = get_expanded_lock()

    # 열쇠 회전과 이동
    for _ in range(4):
        key = rotate(key)
        print(key)
        for x in range(1, N + M):
            for y in range(1, N + M):
                if check(x, y, key, expanded_lock):
                    return True
    return False

