import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
INF = int(1e9)

def build_tree():
    for i in range(size, size+N):
        seg_tree[i] = int(input_())
    for i in range(size-1, 0, -1):
        seg_tree[i] = min(seg_tree[i*2], seg_tree[i*2+1])

def query(left, right):
    left += size-1
    right += size
    answer = INF

    while left < right:
        if left % 2:
            answer = min(answer, seg_tree[left])
            left += 1
        if right % 2:
            right -= 1
            answer = min(answer, seg_tree[right])
        left //= 2
        right //= 2

    return answer

N, M = minput()
size = 2 ** (N-1).bit_length()
seg_tree = [INF] * 2 * size
build_tree()

for _ in range(M):
    a, b = minput()
    print(query(a, b))