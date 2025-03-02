from collections import deque

# 입력 받기
n = int(input())
graph = []
shark_x, shark_y = 0, 0
shark_size = 2
fish_count = 0  # 먹은 물고기 수

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:  # 아기 상어 위치 저장
            shark_x, shark_y = i, j
            row[j] = 0  # 상어 위치를 0으로 변경
    graph.append(row)

# 방향 벡터 (위, 왼쪽, 오른쪽, 아래 순)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# BFS 탐색 함수
def bfs(x, y):
    queue = deque([(x, y, 0)])  # (현재 x, 현재 y, 이동 거리)
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    fish_list = []  # 먹을 수 있는 물고기 리스트
    min_dist = float('inf')  # 최소 거리 초기화

    while queue:
        x, y, dist = queue.popleft()

        # 현재 거리가 최소 거리보다 크면 탐색 중단
        if dist > min_dist:
            break

        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:  # 이동 가능
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

                    # 먹을 수 있는 물고기(상어보다 작은 크기) 발견
                    if 0 < graph[nx][ny] < shark_size:
                        fish_list.append((dist + 1, nx, ny))
                        min_dist = dist + 1  # 최소 거리 갱신

    # 먹을 수 있는 물고기가 있으면 정렬 후 반환
    if fish_list:
        fish_list.sort()  # (거리, x좌표, y좌표) 기준 정렬
        return fish_list[0]  # 가장 우선순위가 높은 물고기 반환
    return None

# 시뮬레이션 시작
time = 0

while True:
    result = bfs(shark_x, shark_y)

    if result is None:  # 먹을 물고기가 없으면 종료
        break

    dist, fish_x, fish_y = result
    shark_x, shark_y = fish_x, fish_y  # 상어 이동
    graph[fish_x][fish_y] = 0  # 물고기 먹음
    time += dist  # 이동 거리만큼 시간 증가
    fish_count += 1  # 먹은 물고기 개수 증가

    # 상어 크기 증가
    if fish_count == shark_size:
        shark_size += 1
        fish_count = 0

# 결과 출력
print(time)
