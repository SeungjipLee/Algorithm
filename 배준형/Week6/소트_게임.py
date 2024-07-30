# 반드시 K 개의 수를 뒤집어야함
# 5 4 3 2 1 이고 K 가 3이면 2, 1 은 선택불가
# 5 2 3 4 1

# 5 4 3 2 1
# 5 4 1 2 3
# 1 4 5 2 3
#   2 5 4 3
#     3 4 5

# 최솟값 찾기
# 최솟값 앞으로 보내는 일 하기

# 구상
# 맨 처음 입력받은 위치 순서 맵에 기록하기
# 정렬헤서 제일 작은 친구부터 앞으로 보내기
# 보내는 로직
# 작은 친구 뒤집어야하니까 K 칸 앞에서 뒤집을 수 있는지 확인
# 뒤집을 수 있으면 뒤집고
# 안되면 한칸 앞으로 이동하게 해보기

import sys
def minput(): return map(int, sys.stdin.readline().split())

N, K = minput()
# arr = minput()
arr = []
idx_dict = {}

for i, a in enumerate(minput()):
    arr.append([a, i])
    idx_dict[i] = i

sorted_arr = sorted(arr, key=lambda x:  x[0])

for a, i in sorted_arr:
    print(a, i)