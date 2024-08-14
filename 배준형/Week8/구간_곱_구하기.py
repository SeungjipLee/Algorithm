# 1,000,000,007
import sys, math
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M, K = minput()

size = 2 * 2 ** (int(math.log2(N)) + 1)
# 곱에 대한 세그먼트 트리 1로 초기화
seg_tree = [1] * size
leaf_idxs = [0] * (N+1)
last_idx = -1

    
def set_segtree(val, cur, idx, s, e):
    if s==e:
        seg_tree[cur] = val 
        leaf_idxs[idx] = cur
        return val
    
    mid = (s+e)//2
    if idx > mid:
        seg_tree[cur] = (seg_tree[2*cur] * set_segtree(val, cur*2+1, idx, mid+1, e)) % 1_000_000_007
    else:    
        left = seg_tree[cur] = set_segtree(val, cur*2, idx, s, mid)
        if cur*2+1 <= last_idx:
            seg_tree[cur] = (left * seg_tree[cur*2+1]) % 1_000_000_007
        else: 
            seg_tree[cur] = left % 1_000_000_007 
    return seg_tree[cur]
    

def get_interval_product(cur, s, e, left, right):
    if e < left or right < s:
        return 1
    
    # left ~ s ~ e ~ right 인 경우 해당 노드를 반환
    if left <= s and right >= e:
        return seg_tree[cur] % 1_000_000_007 
    
    mid = (s+e)//2
    return (get_interval_product(cur*2, s, mid, left, right) * get_interval_product(cur*2+1, mid+1, e, left, right)) % 1_000_000_007
    
    

# N 개의 수 입력받기
for i in range(1, N+1):
    set_segtree(int(input_()), 1, i, 1, N)
last_idx = max(leaf_idxs)
# 수행할 작업 입력받기
# a, b, c
# a == 1: b를 c로 변경 
# a == 2: b부터 c까지 구간 곱 구하기
for _ in range(M+K):
    a, b, c = minput()
    if a == 1:
        set_segtree(c, 1, b, 1, N)
    if a == 2:
        print(get_interval_product(1, 1, N, b, c) % 1_000_000_007)
        
        
# def set_segtree(pre, val, cur, idx, s, e):
#     seg_tree[cur] *= val//pre

#     if s==e:
#         return cur
    
#     mid = (s+e)//2
#     if idx > mid:
#         return set_segtree(pre, val, cur*2+1, idx, mid+1, e)
#     return set_segtree(pre, val, cur*2, idx, s, mid)