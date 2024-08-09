# 각각 높이가 다른 너비가 1 인 직사각형 N개가 나란히 정렬되어 있다
# 히스토그램에서 가장 큰 직사각형은?
# 분류 : 세그먼트트리, 분할정복, 스택

# 
# 세그먼트 트리로 min 값 저장하고
# 오른쪽 으로 탐색하면서 자신의 min 값보다 크거나 같으면 이어서 너비 반환하기
# n 100,000 이고 세그먼트트리를 타는데 기껏해야 트리 한바퀴 돌지 않겠음 2 * log N 들거같음

import sys, math
def minput(): return map(int, sys.stdin.readline().split())

def make_tree(value, cur, idx, s, e):
    if seg_tree[cur] == -1:
        seg_tree[cur] = value
    else:
        seg_tree[cur] = min(seg_tree[cur], value)
        
    if s == e:
        return cur
    
    mid = (s+e)//2
    
    if mid < idx:
        return make_tree(value, cur*2+1, idx, mid+1, e)
    return make_tree(value, cur*2, idx, s, mid)

# 사이즈 췤~!
def size_check(cur, size):
    
    pass
    
while True:
    arr = list(minput())
    
    if arr[0] == 0:
        break
    
    N, *histogram = arr
    seg_size = 2 * 2 ** (int(math.log2(N))+1)
    seg_tree = [-1] * seg_size
    seg_idxs = [0] * N
    answer = 0
    
    for i in range(N):
        seg_idxs[i] = make_tree(histogram[i], 1, i, 0, N-1)
    
    for i in range(N):
        # 하나씩 자신의 오른쪽 보면서 최솟값 x 길이 로 너비 체크
        # 너비가 작아진다면 왼쪽으로 이동 커진다면 오른쪽으로 이동
        # 시작점
        start = seg_idxs[i]
        
        


## 시간초과
# 기본
# 최소높이 너비 체크해가면서 넓이 비교 계속하기
# 시작지점, 현재까지의 최솟값, 현재까지 너비 를 저장하고 한 칸 지날 때마다 꺼내서 갱신

# 개선1 현재 직사각형이 이전 직사각형보다 높이가 같거나 작으면 해당지점은 큐에 넣지 않음 어차피 이전 직사각형에서 계속 재기 때문에
# 개선2 기대값을 주고 q에서 삭제한다면? min 값과 남은 배열크기만큼 다 더해도 맥스보다 작으면 더 이상 돌릴 필요가 없다 추출

# import sys
# from collections import deque
# def minput(): return map(int, sys.stdin.readline().split())

# while True:
#     arr = list(minput())
    
#     if arr[0] == 0:
#         break
    
#     N, *histogram = arr
#     answer = 0
#     q1 = deque()
#     q2 = deque()

#     for i in range(N):
#         # [시작지점 s : start, 최소값 m : min, 현재너비 a : area]
#         now = histogram[i]
#         answer = max(answer, now)
#         # print(q1)
#         # print(q2)
        
#         if i % 2 == 0:
#             while q1:
#                 s, m, a =  q1.popleft()
#                 m = min(now, m)
#                 tmp_a = (i - s + 1) * m
#                 expect_max = m * (N-s)
#                 if a < tmp_a and answer < expect_max:
#                     q2.append([s, m, tmp_a])
#                     answer = max(answer, tmp_a)
#             if i == 0 or now > histogram[i-1]:
#                 q2.append([i, now, now])
#         else:
#             while q2:
#                 s, m, a =  q2.popleft()
#                 m = min(now, m)
#                 tmp_a = (i - s + 1) * m
#                 expect_max = m * (N-s)
                
#                 if a < tmp_a and answer < expect_max:
#                     q1.append([s, m, tmp_a])
#                     answer = max(answer, tmp_a)
#             if now > histogram[i-1]:        
#                 q1.append([i, now, now])

#     print(answer)
        
        