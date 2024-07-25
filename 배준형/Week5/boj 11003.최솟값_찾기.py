import sys, math
def minput(): return map(int, sys.stdin.readline().split())
INF = int(10e9)

N, L = list(minput())
arr = list(minput())
# arr_idx = min_tree 에서 arr 의 i 번째 값이 몇 번째 idx에 있는지
arr_idx = [-1] * N
min_tree = [[INF, -1] for _ in range(L+1)]

def insert_tree(value, idx, tar):
    pre = min_tree[tar][0]
    min_tree[tar] = [value, idx]
    # print()
    # print(value, idx, tar)
    # 최소 힙이 유지 되려면?
    
    # 넣은 값이 이전에 있던거 보다 크면 밑으로 보고 위치 조정
    if value > pre:
        while True:
            if tar*2+1 <= L:
                if value > min_tree[tar*2+1][0] and value > min_tree[tar*2][0]:
                    if min_tree[tar*2+1][0] < min_tree[tar*2][0]:
                        arr_idx[min_tree[tar*2+1][1]] = tar
                        min_tree[tar], min_tree[tar*2+1] =\
                            min_tree[tar*2+1], min_tree[tar]
                        tar = tar*2+1
                    else:
                        arr_idx[min_tree[tar*2][1]] = tar
                        min_tree[tar], min_tree[tar*2] =\
                            min_tree[tar*2], min_tree[tar]
                        tar *= 2
                    continue
                
                if value > min_tree[tar*2+1][0]:
                    # print("come")
                    arr_idx[min_tree[tar*2+1][1]] = tar
                    min_tree[tar], min_tree[tar*2+1] =\
                        min_tree[tar*2+1], min_tree[tar]
                    tar = tar*2+1
                    continue 
                            
            if tar*2 <= L:
                if value > min_tree[tar*2][0]:
                    arr_idx[min_tree[tar*2][1]] = tar
                    min_tree[tar], min_tree[tar*2] =\
                        min_tree[tar*2], min_tree[tar]
                    tar *= 2
                    continue
            break
        
    elif value < pre:
        while True:
            if tar == 1:
                break
            if value < min_tree[tar//2][0]:
                arr_idx[min_tree[tar//2][1]] = tar
                min_tree[tar], min_tree[tar//2] =\
                    min_tree[tar//2], min_tree[tar]
                tar //= 2
                continue
            break
    
    arr_idx[idx] = tar
    # print(min_tree[1:])
    # print(arr_idx)
    
    # 특정 수가 특정 위치에 들어간다
    
        
for i in range(N):
    # 처음 L 개는 순서대로 넣기
    if i < L:
        insert_tree(arr[i], i, i+1)
    else:
        # i-L번 째를 다음 숫자로 덮어 씌우기
        insert_tree(arr[i], i, arr_idx[i-L])
    
    print(min_tree[1][0], end=" ")
    
# INF = int(10e9)
# N, L = list(minput())
# arr = list(minput())

# # 최소힙 트리를 만드는데
# size = 2 ** (int(math.log2(L)) + 1)
# min_tree = [INF] * 2 * size

# def insert_tree(value, cur, idx, s, e):
#     min_tree[cur] = min(min_tree[cur], value)
    
#     if s == e:
#         return cur
#     mid = (s+e)//2
#     if mid < idx:
#         return insert_tree(value, cur*2+1, idx, mid+1, e)
#     return insert_tree(value, cur*2, idx, s, mid)
    
# # def delete_tree(value, cur, idx, s, e):
# #     if s == e:
# #         min_tree[cur] = value
# #         return cur
    
# #     mid = (s+e)//2
# #     if mid < idx:
# #         return delete_tree(value, cur*2+1, idx, mid+1, e)
# #     return delete_tree(value, cur*2, idx, s, mid)

# def update_tree(idx):
#     min_tree[idx] = min(min_tree[idx*2], min_tree[idx*2+1])
#     if idx == 1:
#         return
#     update_tree(idx//2)

# point = -1
# idx_arr = [0] * L
# for i in range(N):
    
#     if i < L:
#         ins_idx = insert_tree(arr[i], 1, i, 0, L-1)
#         idx_arr[i] = ins_idx
#         print(min_tree[1], end=" ")
#         continue
    
#     point += 1
#     if point == L:
#         point = 0
        
#     # del_idx = delete_tree(arr[i], 1, point, 0, L-1)
#     # print()
#     # print(del_idx)
#     # print(min_tree)
#     min_tree[idx_arr[point]] = arr[i]
#     update_tree(idx_arr[point]//2)
    
#     print(min_tree[1], end=" ")
    
    