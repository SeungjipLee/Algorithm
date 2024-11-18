def solution(key, lock):
    # 열쇠 구멍 수
    goal = 0
    
    # 열쇠 시작점을 두고 
    sx, sy = 0, 0
    m = len(key)
    n = len(lock)
    
    # 열쇠 구멍 개수 얻기
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                goal += 1
    
    # 4방향으로 회전해서 키 로직 얻기
    # keys 요소 = [키1, 키2 ]
    # 예제) 왼쪽 중간 (0,1) 좌표의 돌기를 기준으로 상대좌표를 저장
    # 키1 = [[0, 0], [1, 1], [1, 2]]
    # 키2 = 키1을 90도 회전, 키3 = 키1을 180도 회전, 키4 = 키1을 270도 회전
    keys = get_all_key(key, m)
    # print(keys)
    # 열쇠 구멍마다 넣어보기
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                if insert_key(keys, lock, m, n, i, j, goal):
                    return True
    
    if goal == 0:
        return True
    return False

def get_all_key(key, m):
    all_keys = []
    all_keys.extend(get_relative_coordinates(key, m))
    
    for _ in range(3):
        key = rotate_key(key, m)
        all_keys.extend(get_relative_coordinates(key, m))
    
    return all_keys

def get_relative_coordinates(key, m):
    relative_coordinates = []
    tmp = []
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                tmp.append((i, j))
                
    for x, y in tmp:
        tmp_2 = []
        for a, b in tmp:
            tmp_2.append([a-x, b-y])
        relative_coordinates.append(tmp_2)
        
    return relative_coordinates

def rotate_key(key, m):
    rotated_key = []
    for i in range(m):
        tmp = []
        for j in range(m-1, -1, -1):
            tmp.append(key[j][i])
        rotated_key.append(tmp)

    return rotated_key

def insert_key(keys, lock, m, n, x, y, goal):
    
    for candi_key in keys:
        tmp = 0
        crashed = False
        for dx, dy in candi_key:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if lock[nx][ny] == 0:
                tmp += 1
            if lock[nx][ny] == 1:
                crashed = True
        if tmp == goal and not crashed:
            # print(x, y, candi_key)
            return True
    return False
    