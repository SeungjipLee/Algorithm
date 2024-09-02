def solution(m, n, puddles):
    
    graph = [[1]*m for _ in range(n)]
    
    for puddle in puddles:
        y, x = puddle[0]-1, puddle[1]-1
        if x == 0:
            for idx in range(y, m):
                graph[x][idx] = 0
            continue    
        if y == 0:
            for idx in range(x, n):
                graph[idx][y] = 0
            continue
        graph[x][y] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if not graph[i][j]:
                continue
            graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1_000_000_007

    return graph[n-1][m-1] % 1_000_000_007


print(solution(4, 3, [[2,3]]))