def solution(n):
    if n == 1:
        return [[1]]
    dir_dict = {'r':'d', 'd':'l', 'l':'u', 'u':'r'}
    dir = 'r'
    x, y = 0, 0
    answer = [[0]*n for _ in range(n)]
    for i in range(1, n*n+1):
        answer[x][y] = i
        if dir == 'r':
            y += 1
            if y == n-1 or answer[x][y+1]:
                dir = dir_dict[dir]
                
        elif dir == 'd':
            x += 1
            if x == n-1 or answer[x+1][y]:
                dir = dir_dict[dir]
                
        elif dir == 'l':
            y -= 1
            if y == 0 or answer[x][y-1]:
                dir = dir_dict[dir]
        
        else:
            x -= 1
            if x == 0 or answer[x-1][y]:
                dir = dir_dict[dir]

    return answer