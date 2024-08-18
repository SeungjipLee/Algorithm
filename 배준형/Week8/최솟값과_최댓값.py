import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
size = 2 ** (N-1).bit_length()
INF = int(1e9)
max_tree = [0] * 2 * size
min_tree = [INF] * 2 * size

def build_tree():
    for i in range(size, size+N):
        num = int(input_())
        max_tree[i] = num
        min_tree[i] = num

    for i in range(size-1, 0, -1):
        max_tree[i] = max(max_tree[2*i], max_tree[2*i+1])
        min_tree[i] = min(min_tree[2*i], min_tree[2*i+1])

def query(left, right):
    left += (size - 1)
    right += size
    result = [INF, 0]

    while left < right:
        if left % 2:
            result = [min(result[0], min_tree[left]), max(result[1], max_tree[left])]
            left += 1
        if right % 2:
            right -= 1
            result = [min(result[0], min_tree[right]), max(result[1], max_tree[right])]
        left //= 2
        right //= 2
    
    return result

build_tree()

for _ in range(M):
    a, b = minput()
    print(*query(a, b))
    