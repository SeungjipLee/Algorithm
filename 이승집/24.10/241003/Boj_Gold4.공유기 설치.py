import sys

input = sys.stdin.readline
N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

start = 1
end = houses[-1] - houses[0]  # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    now = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= now + mid:
            now = houses[i]
            cnt += 1

    if cnt >= C:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)

"""
처음에는 공유기 위치를 이진탐색을 활용해야하나 고민했는데
-> 최대 차이를 이진탐색으로 찾았음
"""