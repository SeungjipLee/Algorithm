import sys
import math
input_ = sys.stdin.readline

# 나무 심기
# 다음 나무 비용 = 현재 심어져 있는 나무와의 거리의 총합
# 출력
# 2번 나무부터 N번 나무까지를 
# 심는 비용의 곱을 1,000,000,007 로 나눈 값을 출력

# 나무 사이 나무 바깥 
# 두 나무 사이에 있을 때는 어디에 있든 두 나무 거리 차만큼 발생

# 200,000 그루 심어야함
# 이중 포문 불가
# 이진 탐색? .. 
# 자료구조니까 특정 값을 계산해나가는 것일텐데

# 기본
# 한 그루 심을 때마다
# 모든 나무 탐색하며 거리재서 구한다.

# 업그레이드
# 한 그루 심을 때마다
# 좌우 누적함에서 자신이 들어갈 위치 계산
# 근데 누적합필드를 계속 업데이트해야함..
# 맨앞에 계속 넣으면 계속 전체 배열을 업데이트 해줘야함

# 업그레이드2
# 누적합을 써야한다? 세그먼트트리
# 세그먼트 트리를 근데.. 어케 만들고 업데이트 시킴
# 세그 트리 장점 내 값이 바뀌어도 업데이트 시켜줘야하는
# 요소가 logN개임
N = int(input_())
size = 2 ** (int(math.log2(200_000)) + 1)
seg_tree = [[0, 0] for _ in range(2 * size)]
# seg_tree = [누적합, 개수]

def seg_insert(value, s, e, cur, price):
    # print(idx, value, cur)
    seg_tree[cur][0] += value
    seg_tree[cur][1] += 1
    if s == e:
        return price
    mid = (s+e) // 2
    if value > mid:
        # 오른쪽으로 갈 때는 왼쪽 거 더해주기
        # 개수 * 나 - 누적합
        price += value * seg_tree[cur*2][1] - seg_tree[cur*2][0] 
        # print(value, cur, value * seg_tree[cur*2][1] - seg_tree[cur*2][0])
        return seg_insert(value, mid+1, e, cur*2+1, price)
    else:
        # 왼쪽으로 갈때 오른쪽거 더해주기
        # 누적합 - 개수 * 나
        price += seg_tree[cur*2+1][0] - value * seg_tree[cur*2+1][1] 
        # print(value, cur, seg_tree[cur*2+1][0] - value * seg_tree[cur*2+1][1])
        return seg_insert(value, s, mid, cur*2, price)
        
answer = 1
for i in range(N):
    namu = int(input_())
    price = seg_insert(namu, 0, 200000, 1, 0)
    # print(seg_tree)
    if i == 0:
        continue
    # print(i, namu, price)
    # print("result", namu, price)
    answer = (answer * price) % 1_000_000_007
# print(seg_tree)
print(answer )