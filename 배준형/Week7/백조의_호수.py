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
swan = [] # 백조는 어느 물 구역에 있는가?
ices = deque()
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def find_section(section, idx):
    if idx != section[idx]:
        return find_section(section, section[idx])
    return idx

def bfs(graph, visited, ices, sx, sy, s):
    meet_swan = False
    if graph[sx][sy] == "L":
        meet_swan = True
    visited[sx][sy] = True
    graph[sx][sy] = s
    q.append([sx, sy])
    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            if graph[nx][ny] == "L":
                meet_swan = True
                graph[nx][ny] = s
                q.append([nx, ny])
            elif graph[nx][ny] == "X":
                ices.append([nx, ny, s])
                # graph[nx][ny] = s
            elif graph[nx][ny] == ".":
                q.append([nx, ny])
                graph[nx][ny] = s
    
    if meet_swan:
        return True
                
    
# 그래프 전처리
q = deque()
visited = [[False] * M for _ in range(N)]
section_num = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if graph[i][j] != "X":
            if bfs(graph, visited, ices, i, j, section_num):
                swan.append(section_num)
            section_num += 1
water_sections = [i for i in range(section_num+1)]
# 날짜 올리면서 경과보기
day = 0
meet_sections = []
# print(swan)
while True:
    # print(graph)
    # print(water_sections)
    if find_section(water_sections, swan[0]) == find_section(water_sections, swan[1]):
        print(day)
        break
    day += 1
    
    melted = ices
    ices = deque()

    while melted:
        x, y, s = melted.popleft()
        s = find_section(water_sections, s)
        graph[x][y] = s
        
        meet_sections = []
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                if graph[nx][ny] == "X":
                    continue
                if graph[nx][ny] != s:
                    meet_sections.append(graph[nx][ny])
                continue
            
            visited[nx][ny] = True
            ices.append([nx, ny, s])

        meet_sections = list(set(meet_sections))
        for met in meet_sections:
            water_sections[met] = find_section(water_sections, s)
        
