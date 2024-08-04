# N x N 인 땅을 두 사람에게 나누어 주려고 한다
# 나누어주는 땅의 모양은 항상 직사각형이며 변은 축에 평행하다
# 두 땅은 꼭지점 하나에서 만나야 한다
# 1x1 땅에는 각각의 가치를 가지며
# 두 땅은 가치의 합이 같아야 한다
# 분배 가능한 경우의 수를 구하라
# 1x1 땅부터 차례로 크기를 키워가면서 대각선 방향에 같은 크기의 땅이 있는지 확인?
# 브루트포스.. 흠..
# 구현싸움인가? 50x50이 최대니까..

# i, j 돌면서 오른쪽방향 꼭지점만 체크
import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
arr = [list(minput()) for _ in range(N)]
answer = 0

# 일단 누적합 배열 만들어두기
arr_cnt = [[0] * (N+1) for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, N+1):
        if j == 0:
            arr_cnt[i][j] = arr[i-1][j-1]
            continue
        arr_cnt[i][j] = arr_cnt[i][j-1] + arr[i-1][j-1]
        
for i in range(1, N+1):
    for j in range(1, N+1):
        arr_cnt[i][j] += arr_cnt[i-1][j]        
# print(arr_cnt)
# 브루트포스
# 한 점에 대해서 오 밑 대각(오밑)
# (sx0 sy0) (ex0 ey0) (sx1 sy1) (ex1 ey1)
# 네 점만 알면 가능
# 한 점에 대해서 대각선 오른쪽 위아래로 키워가면서 반대편도 키워나가기?..



# # sx0 sy0 정하기 ================== 브루트포스 시간초과 ==================
# for sx0 in range(1, N+1):
#     for sy0 in range(1, N+1):
#         # ex0, ey0 정하기
#         for ex0 in range(sx0, N+1):
#             for ey0 in range(sy0, N+1):
#                 size1 = arr_cnt[ex0][ey0] - arr_cnt[sx0-1][ey0] - arr_cnt[ex0][sy0-1] + arr_cnt[sx0-1][sy0-1]
#                 # sx1, sy1 는 대각선 위 아래 밖에 안됨
#                 # 위쪽인 경우
#                 sx1 = sx0-1
#                 sy1 = ey0+1
#                 for ex1 in range(1, sx1+1):
#                     for ey1 in range(sy1, N+1):
#                         size2 = arr_cnt[sx1][ey1] - arr_cnt[sx1][sy1-1] - arr_cnt[ex1-1][ey1] + arr_cnt[ex1-1][sy1-1]
#                         # print("upside")
#                         # print("sq1", sx0, sy0, ex0, ey0)
#                         # print("sq2", sx1, sy1, ex1, ey1)
#                         # print(size1, size2)
#                         if size1 == size2:
#                             answer+=1 
#                 #아래 쪽인 경우
#                 sx1 = ex0+1
#                 sy1 = ey0+1
#                 # ex1, ey1 정하기
#                 for ex1 in range(sx1, N+1):
#                     for ey1 in range(sy1, N+1):
#                         size2 = arr_cnt[ex1][ey1] - arr_cnt[sx1-1][ey1] - arr_cnt[ex1][sy1-1] + arr_cnt[sx1-1][sy1-1]
#                         # print("sq1", sx0, sy0, ex0, ey0)
#                         # print("sq2", sx1, sy1, ex1, ey1)
#                         # print(size1, size2)
#                         # if size2 > size1:
#                         #     break
#                         if size1 == size2:
#                             answer+=1
#                     # if size2 > size1:
#                     #         break        
# print(answer) 