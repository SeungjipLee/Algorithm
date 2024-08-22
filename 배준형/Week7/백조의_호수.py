# 백조 두 마리가 산다
# 호수가 얼어서 만나지 못한다
# 호수의 물은 상하좌우로 얼음을 하루에 한칸 씩 녹인다
# 두 백조가 만나려면 몇일이 걸리는가? 
# 그냥 좀 날아가서 만나지 ㅡㅡ

# 풀이
# 맵을 bfs 로 탐색하면서 물 구역을 나눈다
# 물 구역중에서 얼음을 만나면 [물구역, 다음날 녹는 얼음이라는 정보] 를 큐에 저장한다
# 큐에서 녹는 얼음 녹이면서 인접한 얼음 녹일 수 있게 정보 업데이트 하기
# 두 물 구역이 만나면 물 구역 업데이트
# 
import sys
from collections import deque
input_ = sys.stdin.readline

N, M = map(int, input_().split())
graph = [list(input_().rstrip()) for _ in range(N)]
swan = 0
ices = deque()
swan_q = deque()
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
sx, sy = 0, 0
visited = [[0]*M for _ in range(N)]
swan_visited = [[0]*M for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            if graph[nx][ny] == "X":
                ices.append([nx, ny])
            else:
                q.append([nx, ny])

def swan_bfs(x, y):
    q2 = deque()
    q2.append([x, y])
    visited[x][y] = 1
    swan_visited[x][y] = 1
    met_swan = False

    while q2:
        x, y = q2.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if swan_visited[nx][ny]:
                continue
            if graph[nx][ny] == "L":
                met_swan = True

            visited[nx][ny] = 1
            swan_visited[nx][ny] = 1

            if graph[nx][ny] == "X":
                swan_q.append([nx, ny])
            else:
                q2.append([nx, ny])

    if met_swan:
        return True
    else:
        return False

for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            swan += 1
            sx, sy = i, j

swan_bfs(sx, sy)
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if graph[i][j] == "X":
            continue
        bfs(i, j)

if swan < 2:
    print(0)
    exit()

day = 0
while True:
    day += 1

    melted = ices
    ices = deque()
    while melted:
        x, y = melted.popleft()
        graph[x][y] = "."
        bfs(x, y)

    melted = swan_q
    swan_q = deque()
    while melted:
        x, y = melted.popleft()
        graph[x][y] = "."
        if swan_bfs(x,y):
            print(day)
            exit()

# import sys
# from collections import deque
# input_ = sys.stdin.readline

# N, M = map(int, input_().split())
# graph = [list(input_().rstrip()) for _ in range(N)]
# swan = [] # 백조는 어느 물 구역에 있는가?
# ices = deque()
# d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# def find_section(section, idx):
#     if idx != section[idx]:
#         return find_section(section, section[idx])
#     return idx

# def bfs(graph, visited, ices, sx, sy, s):

#     if graph[sx][sy] == "L":
#         swan.append(section_num)
#     visited[sx][sy] = True
#     graph[sx][sy] = s
#     q.append([sx, sy])
    
#     while q:
#         x, y = q.popleft()
#         for dx, dy in d:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if visited[nx][ny]:
#                 continue
            
#             visited[nx][ny] = True
#             if graph[nx][ny] == "L":
#                 swan.append(section_num)
#                 graph[nx][ny] = s
#                 q.append([nx, ny])
#             elif graph[nx][ny] == "X":
#                 ices.append([nx, ny, s])
#             elif graph[nx][ny] == ".":
#                 q.append([nx, ny])
#                 graph[nx][ny] = s
                
    
# # 그래프 전처리
# q = deque()
# visited = [[False] * M for _ in range(N)]
# section_num = 0
# for i in range(N):
#     for j in range(M):
#         if visited[i][j]:
#             continue
#         if graph[i][j] != "X":
#             bfs(graph, visited, ices, i, j, section_num)
#             section_num += 1
# water_sections = [i for i in range(section_num+1)]
# # 날짜 올리면서 경과보기
# day = 0
# meet_sections = []
# if len(swan) < 2:
#     print(0)
#     exit()

# while True:
#     # print(graph)
#     if find_section(water_sections, swan[0]) == find_section(water_sections, swan[1]):
#         print(day)
#         break
#     day += 1
    
#     melted = ices
#     ices = deque()

#     while melted:
#         x, y, s = melted.popleft()
#         s = find_section(water_sections, s)
#         graph[x][y] = s
        
#         meet_sections = []
#         for dx, dy in d:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if visited[nx][ny]:
#                 if graph[nx][ny] == "X":
#                     continue
#                 if graph[nx][ny] != s:
#                     meet_sections.append(graph[nx][ny])
#                 continue
            
#             visited[nx][ny] = True
#             ices.append([nx, ny, s])

#         meet_sections = list(set(meet_sections))
#         for met in meet_sections:
#             water_sections[met] = find_section(water_sections, s)
#             # water_sections[met] = find_section(water_sections, s)
        
