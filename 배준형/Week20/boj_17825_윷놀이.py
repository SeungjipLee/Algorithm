import sys

answer = 0

def solution():
    global answer
    arr = list(map(int, sys.stdin.readline().split()))

    # 지도1 다음 칸의 인덱스를 가리키고
    # 지도2 해당 칸의 점수를 가리킴
    n = 33
    # route 원소 = [파란화살표있을 때 값 존재, 주사위값만큼 이동했을 떄 인덱스들1, 2, 3, 4, 5]
    route = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0],
            [6, 21], [7, 0], [8, 0], [9, 0], [10, 0],
            [11, 24], [12, 0], [13, 0], [14, 0], [15, 0], 
            [16, 26], [17, 0], [18, 0], [19, 0], [20, 0],
            [32, 0], [22, 0], [23, 0], [29, 0], [25, 0], 
            [29, 0], [27, 0], [28, 0], [29, 0], [30, 0], 
            [31, 0], [20, 0], [0, 0]
            ]
    score = [0, 2, 4, 6, 8,
            10, 12, 14, 16, 18,
            20, 22, 24, 26, 28,
            30, 32, 34, 36, 38, 
            40, 13, 16, 19, 22, 
            24, 28, 27, 26, 25, 
            30, 35, 0]

    visited = [False] * n
    routes = [[0]*6 for _ in range(n)]
    for idx, ro in enumerate(route):
        routes[idx][1] = ro[0]
        nxt = ro[0]
        if ro[1]:
            routes[idx][0] = ro[1]
            routes[idx][1] = ro[1]
            nxt = ro[1]
        
        # print(nxt)
        for i in range(2, 6):
            if nxt == 0:
                break
            nxt = route[nxt][0]
            routes[idx][i] = nxt
            
    print(routes)

    dfs(arr, 0, routes, score, visited, 0, [0, 0, 0, 0])
    
    return answer

def dfs(arr, idx, routes, score, visited, value, horses):
    global answer

    # 말을 확인하고 가능하면 dfs 재귀에 넣기
    # 0 이 여러개면 여러번 넣는건 좀 그런데 어떻게 분기 처리 해야할까
    now = arr[idx]

    for horse in horses:
        nxt = horse+now
        dfs(arr, idx+1, routes, score, visited, value+score[nxt], horses)
        

    return

solution()