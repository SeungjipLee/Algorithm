import sys
import math
import heapq
def minput(): return map(int, sys.stdin.readline().split())
# 이진탐색트리에서 해당 숫자 지우기..

import random

# Function to generate a test case
def generate_test_case():
    a = random.randint(80000, 100000) 
    b = random.randint(1, 100000) 
    if a >= b: 
        return a, b
    else:
        return b, a

for _ in range(1):
    N, K = generate_test_case()
    # N, K = minput()
    # print(N, K )
    arr = [i for i in range(1, N+1)]
    arr_idx = [0] * N
    arr_dict = {}
    t = 2 ** (int(math.log2(N)) + 1)
    # print(t)
    seg_tree = [[0, 0] for _ in range(2*t)]
    # seg_tree = [[0, 0, 0] for _ in range(2*N)]
    # print(seg_tree)
    answer = "<"
    def make_seg(i, s, e):
        # print(i, s, e)
        if s > e:
            return 0
        if s == e:
            seg_tree[i] = [0, 0]
            arr_idx[s] = i
            arr_dict[i] = s
            return 1
        else:
            left = make_seg(i*2, s, (s+e)//2)
            right = make_seg(i*2+1, (s+e)//2+1, e)
            seg_tree[i] = [left, right]
            return left + right
    make_seg(1, 0, N-1)
    # print(arr_idx)
    # print(seg_tree)
    cur = arr_idx[0]
    for _ in range(N):
        # print(cur)
        if _ == 0:
            cnt = K-1
        else:
            cnt = K
        # print(cur, cnt)
        # cnt 가 클때는 계속 위로 보내기
        while True:
            # print(cur, cnt)
            if cnt == 0 or cur == 1:
                break
            if cur % 2 == 0:
                cur //= 2
                # print("**", cur, cnt)
                r = seg_tree[cur][1]
                if r < cnt:
                    cnt -= r
                    continue
                else:
                    cur = cur * 2 + 1
                    break
            else:
                cur //= 2
            # cnt가 오른쪽보다 작다면
            # 내려가서 끝내야지
        # print(cur, cnt)
        if cur == 1:   
            # 맨위에서는 K 좀 깍아내고
            total = seg_tree[1][0] + seg_tree[1][1]
            if cnt > total:
                cnt %= total
            # 좌우 체크
            if cnt > seg_tree[1][1]:
                cur = 3
                cnt -= seg_tree[1][1]
            else:
                cur = 2
            # print("hoi", cur, cnt)
        if cnt == 0:
            cnt = 1    
        # cnt 가 작을때는 아래로 보내기
        while cnt != 0:
            if seg_tree[cur] == [0, 0]:
                cnt -= 1
                continue
            # print(seg_tree[cur][1])
            if seg_tree[cur][0] < cnt:
                cnt -= seg_tree[cur][0]
                cur *= 2
                cur += 1
            else:
                cur *= 2
        
        
        # 도착지점 나올거아니냐
        # 도착지점 0 만들고 업데이트하기
        # seg_tree[cur] = [0, 0, 0]
        pre = cur
        while cur != 1:
            if cur % 2 == 0:
                seg_tree[cur//2][0] -= 1
            else:
                seg_tree[cur//2][1] -= 1
            cur //= 2
        cur = pre
        
        answer += str(arr_dict[pre]+1)
        if _ != N-1:
            answer += ", "
        else:
            answer += ">"
            
        # print("deleted ", arr_dict[pre]+1)
        # print(seg_tree)
    # print(answer)
    
    



# 세그먼트 트리에 오른쪽이 몇개 있는지에 대한 정보를 담는다면?
# 

# N 명이 원을 이루며 앉아 있다.
# 양의 정수 K, 순서대로 K 번째 사람을 제거한다
# 원을 따라 나머지 사람들로 하여금 계속해서 K 번째 사람을 제거한다
# 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.

# 1 <= K <= N <= 100,000

# K 번째 인 사람을 
# 최대 n log n 시간 안에 찾아야함
# log2(100,000) = 16.6

# 제한시간 0.15초 파이썬 0.75초
# 1500만 연산안에 해결

# 검색, 제거

# 10명이 있어 3번째 사람제거
# 12345678910
# 3을 제거
# 12*45678910
# 12 45*78910
# 12 45 78*10
# 1* 45 78 19

# 나머지?
# 제거된 수에서 더해나가면?
# 10 7
# 7 4 -> 1 4~1 사이에 7이 없음
# 12345678910
# 123456 8910
# 123 56 8910
# 1*3 56 8910

# 남은 수의 개수
# 현재 인덱스
# 다음 인덱스
# 남은수 5 현재 3번째(인덱스2) K 7이면 => (2+9)%5 = 4

# 몇번째를 지워야하는지는 알겠음
# 그 자리에 무슨 숫자가 있는지 어떻게 저장함

# 삭제하면 정렬된 상태여야함.
# 인덱스가 조정되야 함 == 틀린 풀이
# 수가 바뀐다. 0번째 수가 바뀌면 뒤가 모두 바뀐다.
# => 세그먼트 트리로 수를 변경하고 합을 변경해도 lgN