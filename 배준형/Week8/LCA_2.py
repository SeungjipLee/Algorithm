# 편향문제를 해결하거나 새로운 풀이법을 찾거나
# 희소배열. 특정 정점에서 1, 2, 4, 8, 16, ... 2의 배수만큼 이동했을 때 도착하는 지점을 미리저장해두고 사용하기
# 희소배열을 저장한다
# 찾고자 하는 두 노드의 깊이에서 일단 둘의 깊이를 맞춘다
# 희소배열에서 제일 먼 곳부터 부모가 다를 때 까지 내려간다

# 깊이가 19 24 인 두 노드가 있다고 하자 그러면
# 19 19 로 맞추고 2의 제곱수인 16칸 위로 올라간다 깊이 3에서 둘의 부모가 같은지 비교
# 다르다면 또 2의 제곱수 중 최대값만큼 올라가고
# 같다면 2를 나눈 8칸 위를 다시 본다 깊이 11에서 부모가 같은지 비교
# ~~반복~~

# A - B - C - D - E
# 10번 노드의 부모 = 8
# parent[E][0] = D
# parent[E][1] = parent[D][0] = C
# parent[E][2] = parent[C][1]

import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_()) # 노드의 수
adj_ls = [[] for _ in range(N+1)] # 간선 정보
parents = [{} for _ in range(N+1)] # 이진 탐색 부모 정보
rank = [0] * (N+1) # 노드별 깊이 정보
rank[1] = 1 # 루트노드 깊이 초기화

def set_tree():
    q = deque()
    q.append(1)
    visited = [False] * (N+1)
    
    while q:
        now = q.popleft()
        visited[now] = True
        
        for nxt in adj_ls[now]:
            if visited[nxt]:
                continue
            rank[nxt] = rank[now] + 1
            set_parents(nxt, now)
            q.append(nxt)

def set_parents(node, pnode):
    parents[node][0] = pnode
    
    i = 0
    while True:
        p = parents[parents[node][i]].get(i)
        if p != None:
            parents[node][i+1] = parents[parents[node][i]][i]
            i += 1
        else:
            break

def find_parent(node1, node2):
    if node1 == node2:
        return node1
    rank1 = rank[node1]
    rank2 = rank[node2]
    
    while True:
        if rank1 != rank2:
            # 높이 맞추는 로직
            if rank1 > rank2:
                diff = rank1 - rank2
                cal = find_gap(diff)
                node1 = parents[node1][cal]
                rank1 = rank[node1]
            else:
                diff = rank2 - rank1
                cal = find_gap(diff)
                node2 = parents[node2][cal]
                rank2 = rank[node2]
            if node1 == node2:
                return node1
        else:
            # 랭크가 같을 때 로직
            # 높이가 같은데 랭크가 1이다
            if rank1 == 1:
                return 1
            
            # 깊이 1인 노드와의 차이에 대한 2 제곱수 산정
            cal = find_gap(rank1-1)
            # print(node1, node2)
            # print("n", node1, node2)
            while True:
                if cal == -1:
                    break
                tmp1 = parents[node1][cal]
                tmp2 = parents[node2][cal]
                # print(tmp1, tmp2)
                if tmp1 != tmp2:
                    node1 = tmp1
                    node2 = tmp2
                    rank1 = rank[node1]
                    rank2 = rank[node2]
                    break
                else:
                    cal -= 1
            
            if parents[node1][0] == parents[node2][0]:
                break

    return parents[node1][0]

def find_gap(num):
    cnt = 0
    while True:
        if num == 1:
            break
        num //= 2
        cnt += 1
    return cnt

for _ in range(N-1):
    a, b = minput()
    adj_ls[a].append(b)
    adj_ls[b].append(a)
    
set_tree()        

M = int(input_())
for _ in range(M):
    a, b = minput()
    print(find_parent(a ,b))

# 시간 초과
# 부모는 찾을 수 있지만 편향트리의 문제점을 겪음(시간초과)
# import sys
# from collections import deque
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# def find_parents(a, b, parents, rank):
#     rank_a = rank[a]
#     rank_b = rank[b]
    
#     while True:
#         if rank_a != rank_b:
#             if rank_a > rank_b:
#                 rank_a -= 1
#                 a = parents[a]
#             else:
#                 rank_b -= 1
#                 b = parents[b]
#         elif rank_a == rank_b:
#             if a == b:
#                 return a
#             else:
#                 rank_a -= 1
#                 rank_b -= 1
#                 a = parents[a]
#                 b = parents[b]

# N = int(input_())
# parents = [0] * (N+1)
# parents[1] = 1
# rank = [0] * (N+1)
# rank[1] = 1
# adj_ls = [[] for _ in range(N+1)]

# for _ in range(N-1):
#     a, b = minput()
#     adj_ls[a].append(b)
#     adj_ls[b].append(a)

# q = deque()
# visited = [0] * (N+1)
# q.append(1)

# while q:
#     p = q.popleft()
#     visited[p] = 1

#     for c in adj_ls[p]:
#         if visited[c]:
#             continue
#         # 트리의 몇층인지
#         rank[c] = rank[p] + 1
#         parents[c] = p

#         q.append(c)
    
# M = int(input_())
# for _ in range(M):
#     a, b = minput()
#     print(find_parents(a, b, parents, rank))