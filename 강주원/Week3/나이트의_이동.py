import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        continue

    # x1, y1 에서 x2, y2로 간다
    # 나이트는 (-1,2), (1,2), (-1,-2), (1,-2), (-2,-1), (2,-1), (-2,1), (2,1)
    board = [[0]*l for _ in range(l)]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        board[x][y] = 1
        while q:
            x, y = q.popleft()
            for i in [(-1,2), (1,2), (-1,-2), (1,-2), (-2,-1), (2,-1), (-2,1), (2,1)]:
                nx = x + i[0]
                ny = y + i[1]
                if nx < 0 or ny < 0 or nx >= l or ny >= l or board[nx][ny]:
                    continue

                board[nx][ny] = board[x][y] + 1
                if nx == x2 and ny == y2:
                    return
                q.append((nx,ny))

    bfs(x1, y1)
    print(board[x2][y2]-1)