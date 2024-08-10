import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]

# 슬라이딩 윈도우를 위한 준비
window = [0] * (d + 1)
current_kinds = 0

# 처음 k개의 초밥을 윈도우에 추가
for i in range(k):
    if window[ls[i]] == 0:
        current_kinds += 1
    window[ls[i]] += 1

# 쿠폰으로 제공된 초밥이 이미 윈도우에 없으면 추가
if window[c] == 0:
    current_kinds += 1
    window[c] += 1

# 현재까지의 최대 종류 수를 기록
res = current_kinds

# 슬라이딩 윈도우 시작
for i in range(1, n):
    # 윈도우에서 가장 왼쪽의 초밥 제거
    left_index = ls[i - 1]
    window[left_index] -= 1
    if window[left_index] == 0:
        current_kinds -= 1

    # 윈도우에 새롭게 들어올 초밥 추가
    right_index = ls[(i + k - 1) % n]
    if window[right_index] == 0:
        current_kinds += 1
    window[right_index] += 1

    # 쿠폰 초밥이 윈도우에 없으면 종류를 더해줌 
    if window[c] == 0:
        res = max(res, current_kinds+1)
    else:
        res = max(res, current_kinds)

print(res)