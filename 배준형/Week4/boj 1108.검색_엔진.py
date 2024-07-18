import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# SCC 찾기
# 위상정렬로 각 노드 점수 더하기

def tarjan_scc(graph): # scc 그룹을 만들어서 리스트로 반환
    index = 0 
    stack = [] # DFS용 스택
    indices = {} # DFS 로 방문된 순서를 각 노드에 저장
    lowlink = {} # 각 노드가 DFS 방문하면서 만난 가장 낮은 인덱스
    on_stack = {} # DFS 진행중인지 여부 판단
    scc = []
    
    def dfs(v):
        nonlocal index
        # 자기자신을 우선 저장
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        
        if graph.get(v):
            for w in graph[v]:
                if w not in indices: # 아직 미방문인 곳은 다시 dfs 
                    dfs(w)
                    # w 의 dfs 가 종료되고 왔을 때 w 가 만난 제일 작은 노드와 내가 알고 있는 작은 노드 비교
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif on_stack[w]: 
                    # dfs 중이라면 내가 알고 있는 가장 작은 노드와 이 친구 중 누가 더 상위 부모인가
                    lowlink[v] = min(lowlink[v], indices[w])
                
        if lowlink[v] == indices[v]:
            # 같지 않다면 어느 scc에 속해 있다
            # 같다면 scc의 수장 혹은 단일 scc
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            scc.append(component)
    
    for v in graph:
        if v not in indices:
            dfs(v)
    
    return scc

def make_scc_graph(scc, graph):
    node_to_scc = {}
    scc_graph = defaultdict(list)
    
    for index, nodes in enumerate(scc):
        scc_graph[index]
        for node in nodes:
            node_to_scc[node] = index
            
    for u in graph:
        for v in graph[u]:
            if node_to_scc[u] == node_to_scc[v]:
                continue
            scc_graph[node_to_scc[u]].append(node_to_scc[v])

    return scc_graph, node_to_scc

def khan_sort(graph):
    # 위상 정렬. 진입 차수 정하기
    in_degree = {u:0 for u in graph}
    reverse_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            in_degree[u] += 1
            reverse_graph[v].append(u)
    q = deque([u for u in graph if in_degree[u] == 0])
    # print(reverse_graph)
    # print(in_degree)
    # print(q)
    topo_sort = []
    
    while q:
        now = q.popleft()
        topo_sort.append(now)
        for nxt in reverse_graph[now]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    
    return topo_sort

def calculate_score(graph):
    scc = tarjan_scc(graph) 
    scc_graph, node_to_scc = make_scc_graph(scc, graph)
    # print("scc", scc)
    # print("scc_graph", scc_graph)
    # print("node_to_scc", node_to_scc)
    sorted_sites = khan_sort(scc_graph)
    # 위상 정렬된 순서대로 점수 계산 시작
    scores = {u:1 for u in node_to_scc}
    # print(sorted_sites)
    for group_num in sorted_sites:
        for site in scc[group_num]:
            # print(scc[group_num])
            if graph.get(site):
                for v in graph[site]:
                    if node_to_scc[site] == node_to_scc[v]:
                        continue
                    scores[site] += scores[v]
    # print(scores)
    return scores

N = int(input())
infos = []
adj_ls = {}
for _ in range(N):
    site_name, num_links, *linked_sites = input().rstrip().split()
    adj_ls[site_name] = linked_sites
# print(adj_ls)
target = input().rstrip()

scores = calculate_score(adj_ls)
print(scores[target])
# print(scores[target])



# 모든 웹사이트에 1점을 준다
# A 사이트에 B 사이트로 가는 링크가 있다면 A 사이트 점수를 B 사이트에 더한다
# 사이트 마다 해당 사이트로 가는 링크가 있는 사이트를 줌
# 특정 사이트의 점수를 반환하라

# 3
# A 3 B C D
# B 2 C D
# C 1 D
# A
# 위와 같이 입력이 주어질 때 A 는 8 점이다
# A 를 알기 위해선 B C 의 점수가 선 반영되어있어야한다
# 순서에 맞게 조사해야하는 것인가
# 아니면 체인을 걸어서 한 사이트 점수가 오르면 그 사이트와 관련된 사이트의 점수를 올려야 하나

# 헤드를 찾아야하나? 트리에 저장해서 위에서 아래로 내려오게끔
# 하나의 트리에 담기지 않을 수도 있음
# A 에 대한 점수를 찾고자 할 때
# 첫번째 부터 관련된 사이트를 파고 들어가서
# 더 이상 링크를 타고 들어갈 수 없는 지점까지 가서 더하면서
# 정보를 저장하면서 돌아오기
# 맵에 저장된건다시 안해도 되게끔

# N = int(input())
# infos = []
# sites = []
# sites_dict = {}

# i = 0
# for _ in range(N):
#     site_name, num_linked, *linked_sites = input().rstrip().split()
    
#     if sites_dict.get(site_name) == None:
#         sites.append(site_name)
#         sites_dict[site_name] = i
#         i += 1
        
#     link_info = [sites_dict[site_name], []]
    
#     for site in linked_sites:
#         if sites_dict.get(site) == None:
#             sites.append(site)
#             sites_dict[site] = i
#             i += 1
#         link_info[1].append(sites_dict[site])
    
#     infos.append(link_info)

# len_sites = len(sites)
# parents = [-1] * len_sites
# scores = [1] * len_sites


# adj_ls = [[] for _ in range(len_sites)]
# for info in infos:
#     adj_ls[info[0]].extend(info[1])

# # print(adj_ls)
# # SCC, DFS

# for i in range(len_sites):
#     stack = []
#     top = -1
#     visited = [[0] * len_sites for _ in range(len_sites)]
#     # 이미 그룹에 묶인 경우
#     if parents[i] != -1 and parents[i] != i:
#         # print(i)
#         continue
#     stack.append(i)
#     top += 1
#     parent = i
#     parents[i] = parent
#     visited[i][i] = 1

#     while stack:
#         now = stack[top]
#         # parent = parents[stack[top]]
#         for nxt in adj_ls[now]:
#             if nxt == parent:
#                 # print("meet me", now, nxt)
#                 parents[now] = parent
#                 cnt = 0
#                 while stack[top] != parent:
#                     top -= 1
#                     cnt += 1
#                     parents[stack[top]] = parent
#                 top += cnt
#                 # print(parents)
#                 continue
#             if visited[now][nxt]:
#                 continue
#             stack.append(nxt)
#             visited[now][nxt] = 1
#             parents[nxt] = nxt
#             top += 1
#             break
#         else:
#             pre = stack.pop()
#             top -= 1


# target = sites_dict[input().rstrip()]

# def dfs(node):
#     visited = [[0] * len_sites for _ in range(len_sites)]
#     score = 1
#     stack = [node]
#     top = 0
#     visited[node][node] = 1

#     while stack:
#         now = stack[top]
#         for j in adj_ls[now]:
#             if parents[now] == parents[j]:
#                 continue
#             if parents[j] == parents[node]:
#                 continue
#             if visited[now][j]:
#                 continue
#             visited[now][j] = 1
#             stack.append(j)
#             top += 1
#             score += 1
#             break
#         else:
#             stack.pop()
#             top -= 1
#     # print(score)
#     return score

# answer = 1
# for i in adj_ls[target]:
#     if parents[i] == parents[target]:
#         continue
#     else:
#         answer += dfs(i)
# print(sites)
# print(parents)
# print(answer)