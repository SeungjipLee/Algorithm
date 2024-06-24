# 양의 정수 n이 매개변수로 주어집니다. 
# n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 
# 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    arr = [[0 for ar in range(n)] for i in range(n)]
    x = 0
    y = 0
    move = 'd'
    
    if n == 1:
        arr = [[1]]
    else :
        for i in range(n*n):
            arr[x][y] = i+1 # 카운터 체크
    
            if move == 'd':
                y += 1 # 오른쪽으로 이동
                if y == n-1 or arr[x][y+1] != 0:  # 열의 끝 또는 이미 숫자가 대입된곳일때
                    move = 's'
    
            elif move == 's':
                x += 1 # 아래로 이동
                if x == n-1 or arr[x+1][y] != 0:
                    move = 'a'
    
            elif move == 'a':
                y -= 1 # 왼쪽으로 이동
                if y == 0 or arr[x][y-1] != 0:
                  move = 'w'
    
            elif move == 'w':
                x -= 1 # 위로이동
                if x == 0 or arr[x-1][y] != 0:
                  move = 'd'

    return arr