import heapq

N, K = map(int, input().split()) # N : 보석 수, K : 가방 수 1 ~ 300,000
items = [] # 보석 리스트
bags = [] # 가방 리스트, 각 가방에는 최대 한 개의 보석만 넣을 수 있다.

for _ in range(N):
    M, V = map(int, input().split()) # M : 무게, V : 가치 0 ~ 1,000,000
    items.append([M, V])

for _ in range(K):
    C = int(input()) # C : 가방의 최대 무게 0 ~ 100,000,000
    bags.append(C)

items.sort(reverse=True, key=lambda x: x[1])
# print(items)
bags.sort()
answer = 0

def lower_bound(a, x, s, e):
    while s < e:
        mid = (s+e)//2
        if a[mid] < x: s=mid+1
        else: e=mid
    return s

for item in items:
    idx = lower_bound(bags, item[0], 0, K)
    if idx == K:
        continue
    answer += item[1]
    K -= 1
    bags.pop(idx)

print(answer)
# 시간초과
# import bisect
# N, K = map(int, input().split()) # N : 보석 수, K : 가방 수 1 ~ 300,000
# items = [] # 보석 리스트
# bags = [] # 가방 리스트, 각 가방에는 최대 한 개의 보석만 넣을 수 있다.

# for _ in range(N):
#     M, V = map(int, input().split()) # M : 무게, V : 가치 0 ~ 1,000,000
#     items.append([M, V, 0, 0])

# for _ in range(K):
#     C = int(input()) # C : 가방의 최대 무게 0 ~ 100,000,000
#     bags.append(C)

# items.sort(reverse=True, key=lambda x: x[1])
# items.sort(key=lambda x: x[0])
# for i in range(N):
#     items[i][3] = i
# bags.sort()

# def lower_bound(a, x, s, e):
#     while s < e:
#         mid = (s+e)//2
#         if a[mid][0] < x: s = mid+1
#         else: e = mid
#     return s

# answer = 0
# for bag in bags:
#     # 가방에는 담을 수 있는 보석 중 최대 무게 반환
#     idx = lower_bound(items, bag, 0, N)
#     # print(idx)
#     goal = sorted(items[:idx], key=lambda x : (x[1], -x[2]), reverse=True)
#     # print(goal)
#     # print(items)
#     if goal:
#         goal = goal[0]
#         items[goal[3]][2] = 1
#         answer += items[goal[3]][1]

# print(answer)
# 2 3 4

# 3  6  
# 2  3
# 3  2,4
