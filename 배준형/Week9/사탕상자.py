import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
S = 1_000_000
size = 2 ** (S-1).bit_length()
seg_tree = [0] * 2 * size

def set_tree(idx, val):
    idx = size+idx-1
    seg_tree[idx] += val

    while idx > 1:
        seg_tree[idx//2] += val
        idx //= 2

def query(left, right):
    left += size-1
    right += size
    tmp = 0

    while left < right:
        if left % 2:
            tmp += seg_tree[left]
            left += 1
        if right % 2:
            right -= 1
            tmp += seg_tree[right]
        left //= 2
        right //= 2

    return tmp

for _ in range(N):
    cmds = list(minput())
    if cmds[0] == 1:
        # 이진탐색으로 right 범위 정하기
        l = 1
        r = S
        while True:
            if l == r:
                print(l)
                break
            mid = (l+r)//2
            if query(1, mid) >= cmds[1]:
                r = mid
            else:
                l = mid+1
        set_tree(l, -1)
    else:
        set_tree(cmds[1], cmds[2])