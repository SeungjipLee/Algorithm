def solution(wallpaper):
    answer = []
    sx = 60 # 시작 높이
    sy = 60 # 시작 넓이
    ex = -1 # 끝 높이
    ey = -1 # 끝 넓이
    
    wall_list = []
    
    # 2차원배열
    for i1 in range(len(wallpaper)):
        now_list = []
        for j1 in range(len(wallpaper[0])):
            now_list.append(wallpaper[i1][j1])
        wall_list.append(now_list)

    for i in range(len(wall_list)):
        for j in range(len(wall_list[i])):
            if wall_list[i][j] == '#':
                sx = min(sx, i) # 시작높이
                sy = min(sy, j) # 시작 넓이
                ex = max(ex, i+1) # 끝 높이
                ey = max(ey, j+1)# 끝 넓이
    answer = [sx, sy, ex, ey]
    
    return answer