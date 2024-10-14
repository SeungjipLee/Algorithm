from collections import deque

def solution(board):
    answer = int(1e9)
    n = len(board)
    # 특정 좌표에 최단비용으로 갈 수 있다면 갱신해야 함
    cost_graph = [[{i: int(1e9) for i in range(4)} for _ in range(n)] for _ in range(n)]
    
    q = deque()
    # 델타탐색 하 좌 우 상
    dxdy = [[1, 0], [0, -1], [0, 1], [-1, 0]]
    q.append([0, 0, -1])
    for i in range(4):
        cost_graph[0][0][i] = 0
    # print(cost_graph)
    while q:
        x, y, d = q.popleft()
        
        for i in range(4):
            nx, ny = x + dxdy[i][0], y + dxdy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny]:
                continue
            cost = 100
            if d == -1:
                if cost_graph[nx][ny][i] < cost:
                    continue
                cost_graph[nx][ny][i] = cost
                q.append([nx, ny, i])
            else:
                if d != i:
                    cost = 600
                if cost_graph[nx][ny][i] < cost_graph[x][y][d] + cost:
                    continue
                cost_graph[nx][ny][i] = cost_graph[x][y][d] + cost
                q.append([nx, ny, i])
    # print(cost_graph)
    for i in range(4):
        answer = min(answer, cost_graph[n-1][n-1][i])
    return answer