import sys
from heapq import heappop, heappush

# 입력 처리
input = sys.stdin.readline

# 첫 줄: N(노드 수), C(최소 비용)
N, C = map(int, input().split())

# 각 노드의 좌표 저장
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 거리 계산 함수 (유클리드 거리의 제곱)
def calc_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# 프림 알고리즘으로 MST 구성
def prim():
    visited = [False] * N  # 노드 방문 여부
    min_heap = []          # 최소 힙
    visited_count = 0      # 방문한 노드 수
    mst_cost = 0           # 최소 비용

    # 0번 노드부터 시작
    heappush(min_heap, (0, 0))  # 비용, 노드 번호

    while min_heap and visited_count < N:
        cost, node = heappop(min_heap)
        if visited[node]:
            continue

        # 현재 노드를 방문 처리
        visited[node] = True
        mst_cost += cost
        visited_count += 1

        # 연결 가능한 노드를 힙에 추가
        for next_node in range(N):
            if not visited[next_node]:
                distance = calc_distance(points[node], points[next_node])
                if distance >= C:  # 최소 비용 조건 만족해야 연결 가능
                    heappush(min_heap, (distance, next_node))

    # 모든 노드가 연결되었는지 확인
    return mst_cost if visited_count == N else -1

# 결과 출력
print(prim())
