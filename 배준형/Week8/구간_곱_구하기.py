# 1,000,000,007
import sys, math
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

MOD = 1_000_000_007
N, M, K = minput()

size = 2 ** (N-1).bit_length()
seg_tree = [1] * (2 * size)

def build_tree():
    for i in range(size, size+N):
        seg_tree[i] = int(input_())
    for i in range(size-1, 0, -1):
        seg_tree[i] = (seg_tree[i*2] * seg_tree[i*2+1]) % MOD
    
def set_tree(idx, val):
    idx += size-1
    seg_tree[idx] = val
    while idx > 1:
        idx //= 2
        seg_tree[idx] = (seg_tree[idx*2] * seg_tree[idx*2+1]) % MOD
    

def query(left, right):
    result = 1
    left += size - 1
    right += size
    while left < right:
        if left % 2:
            result = (result * seg_tree[left]) % MOD
            left += 1
        if right % 2:
            right -= 1
            result = (result * seg_tree[right]) % MOD
        left //= 2
        right //= 2
    return result

    
build_tree()

for _ in range(M+K):
    a, b, c = minput()
    if a == 1:
        set_tree(b, c)
    if a == 2:
        print(query(b,c) % MOD)
        
        
# def set_segtree(pre, val, cur, idx, s, e):
#     seg_tree[cur] *= val//pre

#     if s==e:
#         return cur
    
#     mid = (s+e)//2
#     if idx > mid:
#         return set_segtree(pre, val, cur*2+1, idx, mid+1, e)
#     return set_segtree(pre, val, cur*2, idx, s, mid)


# import sys, math

# input_ = sys.stdin.readline

# def minput(): 
#     return map(int, input_().split())

# MOD = 1_000_000_007

# # 초기화
# N, M, K = minput()
# size = 2 ** (N-1).bit_length()
# seg_tree = [1] * (2 * size)

# def build_tree():
#     for i in range(size, size + N):
#         seg_tree[i] = int(input_())
#     for i in range(size - 1, 0, -1):
#         seg_tree[i] = (seg_tree[2*i] * seg_tree[2*i+1]) % MOD

# def update(idx, val):
#     idx += size - 1
#     seg_tree[idx] = val
#     while idx > 1:
#         idx //= 2
#         seg_tree[idx] = (seg_tree[2*idx] * seg_tree[2*idx+1]) % MOD

# def query(left, right):
#     result = 1
#     left += size - 1
#     right += size
#     while left < right:
#         if left % 2:
#             result = (result * seg_tree[left]) % MOD
#             left += 1
#         if right % 2:
#             right -= 1
#             result = (result * seg_tree[right]) % MOD
#         left //= 2
#         right //= 2
#     return result

# build_tree()

# for _ in range(M + K):
#     a, b, c = minput()
#     if a == 1:
#         update(b, c)
#     elif a == 2:
#         print(query(b, c))