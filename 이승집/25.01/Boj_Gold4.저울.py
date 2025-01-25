N = int(input())
M = int(input())

# 그래프 초기화
graph = [[0] * N for _ in range(N)]

# 관계 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1  # a > b

# 플로이드-워셜 알고리즘 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 결과 계산
for i in range(N):
    count = 0
    for j in range(N):
        if i != j and not (graph[i][j] or graph[j][i]):
            count += 1
    print(count)
