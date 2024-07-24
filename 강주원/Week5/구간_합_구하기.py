import sys
input = sys.stdin.readline


# 세그먼트 트리 생성
def init(node, start, end):
    # 리프노드면 해당 원소 반환
    if start == end:
        tree[node] = l[start]
    # 재귀하여 이진 트리 생성
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2 + 1, end)
    
    return tree[node]


# 합을 구하는 함수
def subSum(node, start, end, left, right):
    # 겹치지 않는 구간에 대해 합을 구하고자 하면 return
    if left > end or right < start:
        return 0
    
    # 구하고자 하는 범위안에 start~end 가 속해있으면 호출 중지
    if left <= start and end <= right:
        return tree[node]
    
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2 + 1, end, left, right)


# 수의 변경 함수
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff

    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)


n, m, k = map(int, input().split())
tree = [0] * 1000000
l = [int(input()) for _ in range(n)]

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - l[b]
        l[b] = c
        update(1, 0, n-1, b, diff)
    else:
        print(subSum(1, 0, n-1, b-1, c-1))