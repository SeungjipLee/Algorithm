# 문제
# 버스정류장이 있고
# 사람들이 탄다
# a 구간에서 b 구간까지 c 명이 탄다는 정보가 여러개 주어진다 (꼭 모두를 태울 필요는 없다)
# 버스는 최대 태울 수 있는 인원 수가 정해져 있다
# 최대 수용 인원이 5명일 때
# 1번 정거장에서 5번 정거장까지 3명
# 3번 정거장에서 7번 정거장까지 3명 이 탄다는 정보가 주어지면
# 1에서 3명을 태우고 빈자리 만큼 3에서 2명을 태운다
# 마지막정거장까지 태울 수 있는 최대 인원 수를 출력하라

# 어떻게 하면 가장 많은 사람을 태울 수 있는가?

# 최대한 많은 구간을 가져가게끔 하면서
# 인원 적은 순으로 먼저 태우고 
# 겹치는 구간은 추가로 태워가는? 반례가 있으려나

# 버스 최대인원 8명일때
# 1.구간짧은순, 2.인원많은순으로 하면
# 1~6 5명 8~15 5명 5~9 8명 일때
# 5~9가 먼저 타는데 
# 1~6 8~15를 다 태우는게 더 많은 인원을 태워갈 수 있음



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
import sys, math
def minput(): return map(int, sys.stdin.readline().split())

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

