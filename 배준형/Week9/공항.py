import sys
input_ = sys.stdin.readline

# 도킹시킬 위치 찾기
# Gi 가 입력될 때 마다 가능한 큰 수인 게이트 번호를 골라야 함
# 5 가 3번 입력되었다하자
# 첫번째는 5 그 다음은 4 그 다음은 3번 게이트를 도킹시켜줘야함

# Gi 보다 작거나 같은 수중 가장 큰 수

G = int(input_())
P = int(input_())

size = 2 ** (G-1).bit_length()
seg_tree = [0] * 2 * size

for i in range(size, size+G):
    seg_tree[i] = 1
for i in range(size-1, 0, -1):
    seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1] 

def query(idx):
    left = size
    right = idx + size-1

    while True:
        if seg_tree[right]:
            break
        if left == right:
            break
        right -= 1
        left //= 2
        right //= 2   
    
    if seg_tree[right] == 0:
        return False

    while True:
        # print(right)
        if right >= size and seg_tree[right]:
            break
        if right*2+1 < size+G and seg_tree[right*2+1]:
            right = right*2 + 1
        else:
            right *= 2

    seg_tree[right] -= 1
    while right > 1:
        seg_tree[right//2] -= 1
        right //= 2
    # print(seg_tree)

    return True


answer = 0
for _ in range(P):
# for _ in range(4):
    Gi = int(input_())
    if query(Gi):
        answer += 1
    else:
        break
print(answer)