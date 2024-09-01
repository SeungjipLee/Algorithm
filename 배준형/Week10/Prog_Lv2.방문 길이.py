def solution(dirs):
    answer = 0
    x, y = 0, 0 
    d = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
    history = {}
    
    for cmd in dirs:
        nx = x + d[cmd][0]
        ny = y + d[cmd][1]
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        h = str(x)+","+str(y)+","+str(nx)+","+str(ny)
        h2 = str(nx)+","+str(ny)+","+str(x)+","+str(y)
        x, y = nx, ny
        if history.get(h):
            continue
        history[h] = True
        history[h2] = True
        answer += 1
    # print(history)
    return answer