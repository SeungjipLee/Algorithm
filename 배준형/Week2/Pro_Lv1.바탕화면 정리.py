def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 50, 50, 0, 0
    
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i+1)
                rdy = max(rdy, j+1)
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
                
    return answer