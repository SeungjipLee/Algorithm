arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]


def solution(arr):
    # 결과를 저장할 0과 1의 카운트 배열 [0의 개수, 1의 개수]
    result = [0, 0]

    # 재귀 함수 정의
    def compress(x, y, n):
        # 첫 번째 값을 기준으로 모든 값이 같은지 확인
        initial_value = arr[x][y]
        same = True
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != initial_value:
                    same = False
                    break
            if not same:
                break

        # 모든 값이 같다면 그 값을 카운트
        if same:
            result[initial_value] += 1
        else:
            # 4개로 나누어 재귀 호출
            half = n // 2
            compress(x, y, half)  # 1사분면
            compress(x, y + half, half)  # 2사분면
            compress(x + half, y, half)  # 3사분면
            compress(x + half, y + half, half)  # 4사분면

    # 주어진 arr 전체를 시작으로 압축 시도
    compress(0, 0, len(arr))

    return result

print(solution(arr))