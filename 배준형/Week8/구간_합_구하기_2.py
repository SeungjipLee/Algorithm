import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M, K = minput()
size = 2 ** (N-1).bit_length()
seg_tree = [0] * 2 * size
lazy = [0] * 2 * size
arr = [int(input_()) for _ in range(N)]

def build_tree(cur, s, e):
    if s == e:
        seg_tree[cur] = arr[s]
        return seg_tree[cur]

    mid = (s+e)//2
    seg_tree[cur] = build_tree(cur*2, s, mid) + build_tree(cur*2+1, mid+1, e)
    return seg_tree[cur]

def set_lazy(cur, s, e, left, right, val):
    resolve_lazy(cur, s, e)
    if e < left or s > right:
        return
    
    if left <= s and e <= right:
        seg_tree[cur] += val * (e-s+1)
        
        if s != e:
            lazy[cur*2] += val
            lazy[cur*2+1] += val
        return
    
    mid = (s+e)//2
    set_lazy(cur*2, s, mid, left, right, val)
    set_lazy(cur*2+1, mid+1, e, left, right, val)
    seg_tree[cur] = seg_tree[cur*2] + seg_tree[cur*2+1]

def resolve_lazy(cur, left, right):
    if not lazy[cur]:
        return
    
    seg_tree[cur] += lazy[cur] * (right - left + 1)
    if left != right:
        lazy[cur*2] += lazy[cur]
        lazy[cur*2+1] += lazy[cur]
    lazy[cur] = 0

def query(cur, s, e, left, right):
    resolve_lazy(cur, s, e)
    
    if e < left or s > right:
        return 0 
    
    if left <= s and e <= right:
        return seg_tree[cur]
    
    mid = (s+e)//2
    return query(cur*2, s, mid, left, right) + query(cur*2+1, mid+1, e, left, right)


build_tree(1, 0, N-1)

for _ in range(M+K):
    cmds = list(minput())
    if cmds[0] == 1:
        set_lazy(1, 0, N-1, cmds[1]-1, cmds[2]-1, cmds[3])
    else:
        print(query(1, 0, N-1, cmds[1]-1, cmds[2]-1))

# import sys
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# N, M, K = minput()

# size = 2 ** (N-1).bit_length()
# seg_tree = [0] * ( 2 * size )
# rep_tmp = [0] * (N + 1)

# def build_tree():
#     for i in range(size, size+N):
#         seg_tree[i] = int(input_())
#     for i in range(size-1, 0, -1):
#         seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1]

# def set_tree(s, e):
#     for i in range(s, e+1):
#         cur = i + size-1
#         seg_tree[cur] += rep_tmp[i]
#     for i in range(size-1, 0, -1):
#         seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1]
#         # while cur != 1:
#         #     seg_tree[cur//2] += rep_tmp[i]
#         #     cur //= 2

# def query(left, right):
#     answer = 0
#     left += size-1
#     right += size
    
#     while left < right:
#         if left % 2:
#             answer += seg_tree[left]
#             left += 1
#         if right % 2:
#             right -= 1
#             answer += seg_tree[right]
#         left //= 2
#         right //= 2

#     return answer

# build_tree()

# flag = False
# s = 1_000_100
# e = 0
# for _ in range(M+K):
#     cmds = list(minput())
#     if cmds[0] == 1:
#         rep_tmp[cmds[1]] += cmds[3]
#         rep_tmp[cmds[2]+1] += -cmds[3]
#         s = min(s, cmds[1])
#         e = max(e, cmds[2]+1)
#         flag = True
#     else:
#         if flag:
#             for i in range(s, e+1):
#                 rep_tmp[i] += rep_tmp[i-1] 
#             set_tree(s, e)
#         print(query(cmds[1], cmds[2]))
#         flag = False
#         s = 1_000_100
#         e = 0 
#         rep_tmp = [0] * (N+1)