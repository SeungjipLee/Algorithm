def solution(n):
    if n == 1:
        return [[1]]
    answer = [[0] * n for _ in range(n)]
    
    answer[0][0] = 1
    x, y = 0, 0
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0
    value = 2
    
    while True:
        nx, ny = x+dir[d][0], y+dir[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny]:
            d += 1
            if d == 4:
                d = 0
            continue

        answer[nx][ny] = value
        value += 1
        x, y = nx, ny
        if value == n ** 2 + 1:
            break
    
    return answer