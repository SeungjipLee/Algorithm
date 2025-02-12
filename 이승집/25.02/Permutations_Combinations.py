def permutations(arr, r):
    visited = [False] * len(arr)  # 방문 여부 체크 배열
    result = []  # 현재 선택한 요소 저장

    def dfs():
        if len(result) == r:  # r개 선택 완료
            print(result)  # 결과 출력
            return

        for i in range(len(arr)):
            if not visited[i]:  # 아직 방문하지 않은 요소 선택
                visited[i] = True  # 방문 체크
                result.append(arr[i])  # 요소 추가
                dfs()  # 다음 단계 진행
                result.pop()  # 백트래킹 (되돌리기)
                visited[i] = False  # 방문 해제

    dfs()

# 실행 예제
arr = [1, 2, 3]
r = 2
permutations(arr, r)


def combinations(arr, r):
    result = []  # 현재 선택한 요소 저장

    def dfs(start):
        if len(result) == r:  # r개 선택 완료
            print(result)  # 결과 출력
            return

        for i in range(start, len(arr)):  # 현재 인덱스부터 탐색 (중복 방지)
            result.append(arr[i])  # 요소 추가
            dfs(i + 1)  # 다음 요소 선택 (이전 요소는 제외)
            result.pop()  # 백트래킹 (되돌리기)

    dfs(0)

# 실행 예제
arr = [1, 2, 3]
r = 2
combinations(arr, r)

