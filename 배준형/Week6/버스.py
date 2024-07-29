import sys, math
def minput(): return map(int, sys.stdin.readline().split())

# 1. 구간이 짧고
# 2. 명수가 많은
# 그룹부터 집어넣는다?

# 최대 명수인지 어떻게 앎?
# 구간 중간에 들어가는데 어떻게 버스 수용 인원 내인지 앎?
# 어떻게 구간마다 빠르게 현재 인원을 업데이트함

# 기본
# 하나 넣고 나머지 전부 비교하기 넣을 수있는거 넣기 반복
# 50000그룹 20000정거장 
# 50000그룹이 1~20000정거장 1씩 업데이트하면
# 50000 x 20000 = 10 0000 0000 터짐

K, N, C = minput()
cmds = []
for info in range(K):
    cmds.append(list(minput()))

seg_tree = [[0, 0] for _ in range(2 * 2 ** (int(math.log2(N)) + 1))]
seg_idx = [0] * (N+1)
# make tree
for i in range(1, N+1):
    s = 1
    e = N
    cur = 1
    while True:
        seg_tree[cur][1] += C
        if s == e:
            break        
        mid = (s+e)//2
        if mid < i:
            cur = cur*2+1
            s = mid+1
        else:
            cur *= 2
            e = mid
    seg_idx[i] = cur

print(seg_tree)
print(seg_idx)

