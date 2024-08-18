import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M, K = minput()

size = 2 ** (N-1).bit_length()
seg_tree = [0] * ( 2 * size )
rep_tmp = [0] * (N + 1)

def build_tree():
    for i in range(size, size+N):
        seg_tree[i] = int(input_())
    for i in range(size-1, 0, -1):
        seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1]

def set_tree(s, e):
    for i in range(s, e+1):
        cur = i + size-1
        seg_tree[cur] += rep_tmp[i]
    for i in range(size-1, 0, -1):
        seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1]
        # while cur != 1:
        #     seg_tree[cur//2] += rep_tmp[i]
        #     cur //= 2

def query(left, right):
    answer = 0
    left += size-1
    right += size
    
    while left < right:
        if left % 2:
            answer += seg_tree[left]
            left += 1
        if right % 2:
            right -= 1
            answer += seg_tree[right]
        left //= 2
        right //= 2

    return answer

build_tree()

flag = False
s = 1_000_100
e = 0
for _ in range(M+K):
    cmds = list(minput())
    if cmds[0] == 1:
        rep_tmp[cmds[1]] += cmds[3]
        rep_tmp[cmds[2]+1] += -cmds[3]
        s = min(s, cmds[1])
        e = max(e, cmds[2]+1)
        flag = True
    else:
        if flag:
            for i in range(s, e+1):
                rep_tmp[i] += rep_tmp[i-1] 
            set_tree(s, e)
        print(query(cmds[1], cmds[2]))
        flag = False
        s = 1_000_100
        e = 0 
        rep_tmp = [0] * (N+1)