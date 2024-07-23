'''
n*n 보드, 봄보니 게임
1. 색이 다 같지 않을 수도 있다.
2. 색이 다른 인접한 두 칸을 고른다.
3. 고른 칸에 있는 사탕을 서로 교환한다.
4. 모두 같은 색으로 이루어져있는 가장 긴 연속 부분을 모두 먹는다.
애니팡??
RBR
BRBB
0,1과 1,1을 교환하면
RRR
BBBB에서 BBBB만 먹나?
0,0에서 시작해서 우측과 아래쪽만 판단하면 되지 않을까?
예제 1
3
CCP
CCP
PPC
에서 2,1과 2,2를 교환하면
CCP
CCP
PCP 이 되면서 3개짜리 한줄이 최대가 된다.
그럼 교환후 바뀐것 기준으로 행 열을 검사해야한다.
2행, 1열, 2열을 검사한다.
알고리즘 분류는? n의 범위가 50 이하이니 구현 아니면 브루트포스?
'''

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
def check():
    max_cnt = 1  # total_max_cnt
    for i in range(n):
        # 가로
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        # 세로
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt

res = 0
res = max(res, check())
    
# 0,0 에서 시작해서 오른쪽과 아래를 탐색한다.
for i in range(n):
    for j in range(n):
        for k in [(1,0), (0,1)]:
            ni = i + k[0]
            nj = j + k[1]
            # 범위를 벗어나거나 같은 색깔이면 continue
            if ni < 0 or nj < 0 or ni >= n or nj >= n or board[ni][nj] == board[i][j]:
                continue
            
            # 복사후 위치 변경한다.
            board[ni][nj], board[i][j] = board[i][j], board[ni][nj]
            res = max(res, check())
            board[ni][nj], board[i][j] = board[i][j], board[ni][nj]

print(res)