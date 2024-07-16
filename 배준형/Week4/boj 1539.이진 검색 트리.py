import sys, bisect
input = sys.stdin.readline

# 트리를 직접만들며 높이를 재면 시간초과
# 250000개의 숫자를 불러오면서 
# 입력된 수가 (1 ~ logN 의 시간 안에)몇번째 높이인지를 알아야하거나 // 이진 탐색으로 이게 가능한가
# 높이의 합을 반환하는 특별한 로직이 있거나 // 이 경우는 생각해내기가 많이 힘들어보임
# def binary_search(n, s, e):
#     while s < e:
#         mid = (s+e)//2

#         if arr[mid] < n:
#             s = mid + 1
#         else:
#             e = mid
#     return e

N = int(input())
arr = []
hs = [0] * N

for _ in range(N):
    num = int(input())
    # idx = binary_search(num, 0, len(arr))
    idx = bisect.bisect_left(arr, num)
    left = 0
    right = 0
    if idx > 0:
        left = hs[arr[idx-1]]
    if idx < len(arr):
        right = hs[arr[idx]]
    hs[num] = max(left, right) + 1
    arr.insert(idx, num)

print(sum(hs))
# --------------------------------------------------------------------------------------
# # 시간 초과 44 % 
# N = int(input())
# arr = [] # item = [num, heigth, left, right] left,right == 0: None
# # arr.append([int(input()), 1, 0, 0])
# arr.append([N-1, 1, 0, 0])
# len_arr = 1
# answer = 1
# # 새로 입력되는 값의 높이를 알려면 어떻게 해야할까...
# # 배열에 입력되는 첫번째 값을 넣고
# # 다음 들어오는 친구들 부터 이진탐색으로 자기 자리를 찾아감
# # 자기 자리에서 왼쪽 오른쪽 친구를 보고 들어 갈 수 있는 자리를 찾아서 들어간 후 높이를 저장
# def binary_search(n, s, e):
#     # if n == 4:
#     #     print(s, e)
#     mid = (s + e) // 2
#     if s == 0 and e == 1:
#         if arr[s][0] > n:
#             return 0
#         elif arr[e][0] < n:
#             return 2
#         else:
#             return 1
#     if mid == e:
#         if arr[mid][0] < n:
#             return mid + 1
#         else:
#             return mid

#     if arr[mid][0] < n:
#         s = mid + 1
#         return binary_search(n, s, e)
#     else:
#         e = mid - 1
#         return binary_search(n, s, e)
        
    
# for _ in range(N-2, -1, -1):
#     # num = int(input())
#     num = _
#     if len_arr == 1:
#         if arr[0][0] > num:
#             arr[0][2] = 1 
#             arr.insert(0, [num, 2, 0, 0])
#         else:
#             arr[0][3] = 1
#             arr.append([num, 2, 0, 0])
#         len_arr += 1
#         answer += 2
#         continue
    
#     idx = binary_search(num, 0, len_arr-1)
#     if idx == 0:
#         arr[idx][2] = 1
#         arr.insert(idx, [num, arr[idx][1]+1, 0, 0])
#         answer += arr[idx][1]
#     elif idx == len_arr:
#         arr[idx-1][3] = 1
#         arr.insert(idx, [num, arr[idx-1][1]+1, 0, 0])
#         answer += arr[idx][1]
#     else:
#         arr.insert(idx, [num, max(arr[idx-1][1], arr[idx][1])+1, 0, 0])
#         answer += arr[idx][1]
#     #     if not arr[idx-1][3]: # 왼쪽의 오른쪽이 비어있다면
#     #         arr[idx-1][3] = 1
#     #         arr.insert(idx, [num, arr[idx-1][1]+1, 0, 0])
#     #         answer += arr[idx][1]
#     #     else:
#     #         arr[idx][2] = 1
#     #         arr.insert(idx, [num, arr[idx][1]+1, 0, 0])
#     #         answer += arr[idx][1]
            
#     len_arr += 1
#     # print(idx, arr)
    
# print(answer)
# --------------------------------------------------------------------------------------
# 시간 초과 18 % 
# tmp = [0, 0, 0]
# tmp.insert(3, 3)
# print(tmp)

# class Node:
#     def __init__(self, value, left=None, right=None) -> None:
#         self.value = value
#         self.right = right
#         self.left = left
        
    
# class BST:
#     answer = 0
    
#     def __init__(self, head) -> None:
#         self.head = head
    
#     def insert(self, num):
#         self.depth = 2
        
#         if not self.head:
#             self.head = Node(num)
#             self.answer += 1
#             return True
        
#         self.cn = self.head

#         while True:
#             if num < self.cn.value:
#                 if self.cn.left:
#                     self.cn = self.cn.left
#                     self.depth += 1
#                 else:
#                     self.cn.left = Node(num)
#                     self.answer += self.depth
#                     print(num, self.depth)
#                     return True
#             else:
#                 if self.cn.right:
#                     self.cn = self.cn.right
#                     self.depth += 1
#                 else:
#                     self.cn.right = Node(num)
#                     self.answer += self.depth
#                     print(num, self.depth)
#                     return True
                    

# N = int(input())

# tree_bs = [0] * (N+1)
# tree_bs_cnt = [0] * (N+1)
# bst = BST(None) 
# for _ in range(N):
#     bst.insert(int(input()))
    
# print(bst.answer)

   