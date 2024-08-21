# 1 2 3
# 4 5 6
# 7 8 0
# 
# 9개의 숫자가 있고 상하좌우 중에 빈칸이 있으면 이동시킬 수 있다
# 초기상태가 되려면 최소 몇번 이동시켜야 하는가?
# BFS
# 4 1 2
# 6 5 3
# 0 7 8
import sys, copy
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

puzzle_dict = {}


            
def bfs():
    q = deque()
    graph = "123456780"
    puzzle_dict[graph] = 0
    q.append([2, 2, 0, graph])

    while q:
    # for i in range(1):
        x, y, d, graph = q.popleft()
        idx1 = x*3 + y
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            idx2 = nx*3 + ny
            s, e = min(idx1, idx2), max(idx1, idx2)
            key = graph[0:s] + graph[e] + graph[s+1:e] + graph[s] + graph[e+1:] 
            if puzzle_dict.get(key) != None:
                continue
            puzzle_dict[key] = d+1
            q.append([nx, ny, d+1, key])

bfs()

k = "".join("".join(list(input_().rstrip().split())) for _ in range(3))
if puzzle_dict.get(k) != None:
    print(puzzle_dict[k])
else:
    print(-1)


# def bfs():
#     q = deque()
#     graph = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"]]
#     puzzle_dict["".join("".join(i) for i in graph)] = 0
#     q.append([2, 2, 0, copy.deepcopy(graph)])

#     while q:
#         x, y, d, graph = q.popleft()
#         for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
#                 continue
#             graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
#             key = "".join("".join(i) for i in graph)
#             if puzzle_dict.get(key) != None:
#                 graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
#                 continue
#             # print(key)
#             puzzle_dict[key] = d+1
#             q.append([nx, ny, d+1, copy.deepcopy(graph)])
#             graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]