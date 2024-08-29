import sys
def minput(): return map(int, sys.stdin.readline().split())

N, M = minput()
size = 2 ** (N-1).bit_length()
seg_tree = [0] * 2 * size

def set_tree(i, k):
    idx = i+size-1
    cur_num = seg_tree[idx]
    seg_tree[idx] = k
    
    while idx > 1:
        seg_tree[idx//2] -= cur_num
        seg_tree[idx//2] += k
        idx //= 2

def query(i, j):
    left = min(i, j) + size - 1
    right = max(i, j) + size
    tmp = 0

    while left < right:
        if left & 1:
            tmp += seg_tree[left]
            left += 1
        if right & 1:
            right -= 1
            tmp += seg_tree[right]
        left //= 2
        right //= 2

    return tmp
            

for _ in range(M):
    a, b, c = minput()
    if a == 0:
        print(query(b, c))

    elif a == 1:
        set_tree(b, c)