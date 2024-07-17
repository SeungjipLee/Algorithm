import sys
input = sys.stdin.readline

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

N = int(input())
infos = []
sites = []
sites_dict = {}

i = 0
for _ in range(N):
    site_name, num_linked, *linked_sites = input().rstrip().split()
    
    if sites_dict.get(site_name) == None:
        sites.append(site_name)
        sites_dict[site_name] = i
        i += 1
        
    link_info = [sites_dict[site_name], []]
    
    for site in linked_sites:
        if sites_dict.get(site) == None:
            sites.append(site)
            sites_dict[site] = i
            i += 1
        link_info[1].append(sites_dict[site])
    
    infos.append(link_info)

len_sites = len(sites)
parents = [-1] * len_sites
scores = [1] * len_sites


adj_ls = [[] for _ in range(len_sites)]
for info in infos:
    adj_ls[info[0]].extend(info[1])

# print(adj_ls)
# SCC, DFS

for i in range(len_sites):
    stack = []
    top = -1
    visited = [[0] * len_sites for _ in range(len_sites)]
    # 이미 그룹에 묶인 경우
    if parents[i] != -1 and parents[i] != i:
        # print(i)
        continue
    stack.append(i)
    top += 1
    parent = i
    parents[i] = parent
    visited[i][i] = 1

    while stack:
        now = stack[top]
        # parent = parents[stack[top]]
        for nxt in adj_ls[now]:
            if nxt == parent:
                # print("meet me", now, nxt)
                parents[now] = parent
                cnt = 0
                while stack[top] != parent:
                    top -= 1
                    cnt += 1
                    parents[stack[top]] = parent
                top += cnt
                # print(parents)
                continue
            if visited[now][nxt]:
                continue
            stack.append(nxt)
            visited[now][nxt] = 1
            parents[nxt] = nxt
            top += 1
            break
        else:
            pre = stack.pop()
            top -= 1


target = sites_dict[input().rstrip()]

def dfs(node):
    visited = [[0] * len_sites for _ in range(len_sites)]
    score = 1
    stack = [node]
    top = 0
    visited[node][node] = 1

    while stack:
        now = stack[top]
        for j in adj_ls[now]:
            if parents[now] == parents[j]:
                continue
            if parents[j] == parents[node]:
                continue
            if visited[now][j]:
                continue
            visited[now][j] = 1
            stack.append(j)
            top += 1
            score += 1
            break
        else:
            stack.pop()
            top -= 1
    # print(score)
    return score

answer = 1
for i in adj_ls[target]:
    if parents[i] == parents[target]:
        continue
    else:
        answer += dfs(i)
print(sites)
print(parents)
print(answer)