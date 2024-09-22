# import sys
# from collections import deque
# from itertools import combinations
# input = sys.stdin.readline

# n, m, d = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]


# def bfs(archers):
#     new_board = [i[:] for i in board]
#     kill = 0

#     for turn in range(n-1, -1, -1):
#         death_note = set()

#         for archer in archers:
#             q = deque()
#             q.append([turn, archer, 1])

#             while q:
#                 x, y, dist = q.popleft()
#                 if new_board[x][y]:
#                     death_note.add((x, y))
#                     break

#                 if dist >= d:
#                     continue

#                 for i in [(0,-1), (-1,0), (0,1)]:
#                     nx = x + i[0]
#                     ny = y + i[1]
#                     if 0 <= nx < n+1 and 0 <= ny < m:
#                         q.append([nx, ny, dist+1])


#         for x, y in death_note:
#             new_board[x][y] = 0
#             kill += 1

#     return kill


# comb = combinations([i for i in range(m)], 3)
# res = 0
# for c in comb:
#     res = max(res, bfs(c))

# print(res)
print(100*(0.8**133))