# 각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 
# 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.

# 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 
# board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 
# return 하도록 solution 함수를 완성해 주세요.

# 이웃한 칸들 중 몇 개의 칸이 같은 색으로 색칠되어 있는지 확인하는 과정은 다음과 같습니다.

def solution(board, h, w):
    answer = 0
    # 높이 오 / 위 / 아 / 왼
    dh = [0, 1, -1, 0]
    # 넓이
    dw = [1, 0, 0, -1]
    # 선택된 색
    now = board[h][w]
    
    for i in range(4):
        # 높이가 0보다 높고 최대숫자보다 작을때
        print(h + dh[i])
        print(w + dw[i])
        if 0 <= h + dh[i] < len(board) and 0 <= w + dw[i] < len(board[0]):
            print(board[h + dh[i]][w + dw[i]])
            if board[h + dh[i]][w + dw[i]] == now:
                answer += 1
    
    
    return answer