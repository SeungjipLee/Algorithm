import sys, math
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
arr = list(minput())
arr_idx = [0] * (N+1)
seg_tree = [0] * 2 * 2 ** (int(math.log2(N)) + 1)
M = int(input_())
max_idx = -1

def insert_tree(value, cur, idx, s, e):
    seg_tree[cur] += value
    if s == e:
        return cur
    
    mid = (s+e)//2
    if mid < idx:
        return insert_tree(value, cur*2+1, idx, mid+1, e)
    return insert_tree(value, cur*2, idx, s, mid)

def find_unit(value, cur, total, s, e):
    if s == e:
        return s
    mid = (s+e)//2
    if total + seg_tree[cur*2] < value:
        return find_unit(value, cur*2+1, total+seg_tree[cur*2], mid+1, e)

    return find_unit(value, cur*2, total, s, mid)

def update_tree(value, idx):
    seg_tree[idx] += value
    if idx == 1:
        return
    return update_tree(value, idx//2)

for i in range(N):
    arr_idx[i+1] = insert_tree(arr[i], 1, i+1, 1, N)
max_idx = max(arr_idx)
# print(arr_idx)
# print(seg_tree)
for _ in range(M):
    cmd = list(minput())
    if cmd[0] == 1:
        update_tree(cmd[2], arr_idx[cmd[1]])
        continue
    # print(seg_tree)
    if cmd[0] == 2:
        print(find_unit(cmd[1], 1, 0, 1, N))
    
