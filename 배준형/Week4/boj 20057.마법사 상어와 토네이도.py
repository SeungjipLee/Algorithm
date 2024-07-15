import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
d = 0 # direction
move = 0 # how many moves for this direction
move_max = 1 # if move == move_max: change direction
cnt = 0 # if cnt == 2: move_max += 1
x, y = N//2 , N//2 # start position
answer = 0 # amount of dust out of map

# until tornado reach at 0, 0
# while x != 0 and y != 0:
while True:
    if x == 0 and y == 0:
        break

    # 이동에 대한 처리
    dx, dy = dir[d]
    nx, ny = x + dx, y + dy
    x, y = nx, ny
    
    # 먼지에 대한 처리
    dust = graph[x][y]
    dust_remain = dust
    graph[x][y] = 0
    dust_blow = [
        [[-2, 0, 0.02], [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01], [0, -2, 0.05],
         [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01], [2, 0, 0.02], [0, -1, 1]],
        [[-1, -1, 0.01], [-1, 1, 0.01], [0, -2, 0.02], [0, -1, 0.07], [0, 1, 0.07], 
         [0, 2, 0.02], [1, -1, 0.1], [1, 1, 0.1], [2, 0, 0.05], [1, 0, 1]],
        [[-2, 0, 0.02], [-1, -1, 0.01], [-1, 0, 0.07], [-1, 1, 0.1], 
         [0, 2, 0.05], [1, -1, 0.01], [1, 0, 0.07], [1, 1, 0.1], [2, 0, 0.02], [0, 1, 1]],
        [[-2, 0, 0.05], [-1, -1, 0.1], [-1, 1, 0.1], [0, -2, 0.02],
         [0, -1, 0.07], [0, 1, 0.07], [0, 2, 0.02], [1, -1, 0.01], [1, 1, 0.01], [-1, 0, 1]]
        ]
    for dx, dy, ratio in dust_blow[d]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            if ratio == 1:
                answer += dust_remain
                continue
            answer += int(dust * ratio)
            dust_remain -= int(dust * ratio)
        else:
            if ratio == 1:
                graph[nx][ny] += dust_remain
                continue
            graph[nx][ny] += int(dust * ratio)
            dust_remain -= int(dust * ratio)
    
    move += 1
    if move == move_max:
        move = 0
        d += 1
        cnt += 1
        if d == 4:
            d = 0
    
    if cnt == 2:
        move_max += 1
        cnt = 0
        
    
print(answer)