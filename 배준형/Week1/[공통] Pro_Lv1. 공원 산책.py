def solution(park, routes):
    n, m = len(park), len(park[0])
    graph = [[0] * m for _ in range(n)]
    x, y = 0, 0
    direction = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j
                graph[i][j] = 1
            if park[i][j] == "X":
                graph[i][j] = -1
    
    for order in routes:
        sx, sy = x, y
        dir, dis = order.split()
        dx, dy = direction[dir]
        dis = int(dis)
        
        for _ in range(dis):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                x, y = sx, sy
                break
            if graph[nx][ny] == -1:
                x, y = sx, sy
                break
            x, y = nx, ny
                
    answer = [x, y]
    return answer