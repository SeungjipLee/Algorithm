import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
INF = int(1e6)

def build_tree():
    for i in range(size, size+N):
        seg_tree[i] = [arr[i-size], arr[i-size], 1]
    for i in range(size-1, 0, -1):
        seg_tree[i] = [min(seg_tree[2*i][0], seg_tree[2*i+1][0]), max(seg_tree[2*i][1], seg_tree[2*i+1][1]), seg_tree[2*i][2] + seg_tree[2*i+1][2]]

def query(idx):
    val = seg_tree[size+idx][0]
    left = idx + size + 1
    right = size + N
    tmp = 0
    while left < right:
        if left % 2:
            tmp += lower_count(left, val)
            left += 1
        if right % 2:
            right -= 1
            tmp += lower_count(right, val)
        left //= 2
        right //= 2
    
    return tmp

def lower_count(idx, val):
    if seg_tree[idx][1] < val:
        return seg_tree[idx][2]
    
    if seg_tree[idx][0] > val:
        return 0
    
    return lower_count(idx*2, val) + lower_count(idx*2+1, val)

N = int(input_())
arr_A = list(minput())
arr_B = list(minput())
dict_B = {}
arr = [0] * N
for i in range(N):
    dict_B[arr_B[i]] = i
for i in range(N):
    arr[i] = dict_B[arr_A[i]]

size = 2 ** (N-1).bit_length()
seg_tree = [[INF, 0, 0] for _ in range(2*size)]

build_tree()
answer = 0
for i in range(N):
    answer += query(i)

print(answer)