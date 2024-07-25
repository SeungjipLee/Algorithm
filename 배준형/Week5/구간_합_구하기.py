import sys, math
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M, K = minput()
arr = []
# arr 의 i 번째 숫자는 tree에 몇 번 인덱스로 저장되어있는지
arr_idx = [0] * N

size = 2 ** (int(math.log2(N)) + 1)
seg_tree = [0] * 2 * size

def make_tree(value, cur, idx, s, e):
    seg_tree[cur] += value
    
    if s == e:
        return cur
    
    mid = (s+e)//2
    if mid < idx:
        return make_tree(value, cur*2+1, idx, mid+1, e)
    return make_tree(value, cur*2, idx, s, mid)
    
def delete_tree(cur, idx, s, e):
    if s == e:
        return cur
    
    mid = (s+e)//2
    if mid < idx:
        return delete_tree(cur*2+1, idx, mid+1, e)
    return delete_tree(cur*2, idx, s, mid)

def update_tree(diff, idx):
    seg_tree[idx] -= diff
    
    if idx == 1:
        return
    update_tree(diff, idx//2)
    
def get_right_sum(idx, total):
    if idx == 1:
        return total
    
    if idx % 2 == 1:
        return get_right_sum(idx//2, total)
    return get_right_sum(idx//2, total+seg_tree[idx+1])

for i in range(N):
    v = int(input_())
    i_ = make_tree(v, 1, i, 0, N-1)
    arr_idx[i] = i_
    
for _ in range(M+K):
    cmd, a, b = minput()
    
    if cmd == 1:
        del_ = delete_tree(1, a-1, 0, N-1)
        tmp = seg_tree[del_]
        update_tree(tmp-b, del_)
        continue
    
    a_ = get_right_sum(arr_idx[a-1], 0)
    b_ = get_right_sum(arr_idx[b-1], 0)
    
    print(seg_tree[arr_idx[a-1]] + a_ - b_)