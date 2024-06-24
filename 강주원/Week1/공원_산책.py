def solution(park, routes):
    x_length = len(park)
    y_length = len(park[0])
    for i in range(x_length):
        for j in range(y_length):
            if park[i][j] == 'S':
                x, y = i, j
    
    for i in routes:
        dist = int(i[2])
        dir = i[0]
        temp_x, temp_y = x, y
        if dir == 'E':
            for j in range(dist):
                if temp_y+1 == y_length or park[temp_x][temp_y+1] == 'X':
                    temp_y = y
                    break
                temp_y += 1
        elif dir == 'S':
            for j in range(dist):
                if temp_x+1 == x_length or park[temp_x+1][temp_y] == 'X':
                    temp_x = x
                    break
                temp_x += 1
        elif dir == 'W':
            for j in range(dist):
                if temp_y-1 == -1 or park[temp_x][temp_y-1] == 'X':
                    temp_y = y
                    break
                temp_y -= 1
        else:
            for j in range(dist):
                if temp_x-1 == -1 or park[temp_x-1][temp_y] == 'X':
                    temp_x = x
                    break
                temp_x -= 1
        x, y = temp_x, temp_y

    answer = [x,y]
    return answer

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))