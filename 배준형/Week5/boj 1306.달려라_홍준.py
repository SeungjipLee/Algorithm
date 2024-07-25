# 배열 길이 N 
# 시야 앞뒤로 M-1
# 시야안에 가장 큰 수 출력
# 1 <= M <= N <= 1,000,000
# 최대 100만번 특정 크기의 배열에서 최댓값을 알아야 함..

# 세그먼트트리에 누적합을 저장해둔다
# 슬라이딩 윈도우로 M 길이만큼 합을 보고 

import sys, math
def minput(): return map(int, sys.stdin.readline().split())

def insert_tree(value, cur, idx, s, e):
    max_tree[cur] = max(value, max_tree[cur])

    if s == e:
        return
    mid = (s+e)//2
    
    if mid < idx:
        return insert_tree(value, cur*2+1, idx, mid+1, e)
    
    return insert_tree(value, cur*2, idx, s, mid)
    
def delete_tree(cur, idx, s, e):
    # idx 지우기 = 0으로 업데이트
    if s == e:
        max_tree[cur] = 0
        return cur
    mid = (s+e)//2
    
    if mid < idx:
        return delete_tree(cur*2+1, idx, mid+1, e)
    
    return delete_tree(cur*2, idx, s, mid)

def update_tree(idx):
    # print("update", idx)
    max_tree[idx] = max(max_tree[2*idx], max_tree[2*idx+1])
    if idx == 1:
        return
    return update_tree(idx//2)

N, M = minput()
arr = list(minput())
size = 2 ** (int(math.log2(2*M-1)) + 1)
max_tree = [0] * 2 * size
# 리프노드가 M 개인 트리를 만드는데
# 맨 위에는 가장 큰 값을 저장
# 앞에서부터 지우면서 다음값을 저장하고 트리 업데이트

for i in range(min(N, 2*M-1)):
    insert_tree(arr[i], 1, i, 0, 2*M-1)

# 몇번 반복하냐
# M 에서 시작해서 N-M+1 까지
# 10 이고 시야가 3이야
# 0 1 (2) 3 4 !5 6 (7) 8 !9 
# 0~4는 이미 바라봤으니 5부터 9까지 넣으면 됨
print(max_tree[1], end=" ")
# print(max_tree)
point = -1
for i in range(2*M-1, N):
    point += 1
    if point == 2*M-1:
        point = 0
    # print("point", point)
    del_idx = delete_tree(1, point, 0, 2*M-1)
    update_tree(del_idx//2)
    # print("del", del_idx)
    insert_tree(arr[i], 1, point, 0, 2*M-1)
    print(max_tree[1], end=" ")
    # print(max_tree)
    

