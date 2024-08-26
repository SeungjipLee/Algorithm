import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
'''
좌석은 양 옆으로만 교환 가능하다.
n = 1이면 1 = 1
n = 2이면 1 2, 2 1 = 2
n = 3이면 1 2 3, 1 3 2, 2 1 3 = 3
n = 4이면 1 2 3 4, 1 2 4 3, 1 3 2 4, 2 1 3 4, 2 1 4 3 = 5
1 2 3 5 8 피보나치
dp[n] = dp[n-2] + dp[n-1]

vip가 들어가게 되면 
1 2 3 4 5 6 7 8 9 에서 vip가 4번을 선택하게 되면
1 2 3 [4] 5 6 7 8 9 에서 2개의 집단으로 나뉘게 되고 dp[3] * dp[5]의 경우의 수가 나온다
마찬가지로
1 [2] 3 [4] 5 6 7 8 9 이면 dp[1] * dp[1] * dp[5]

그럼 vip인지 아닌지를 분간하는 배열을 만들어보자
0 0 0 0 0 0 0 0 0 0
is_vip = 0 0 1 0 1 0 0 1 0 0
계수 = 0
경우의수 = 1
for i in range(1, n+1):
    if is_vip[i] == 0:
        계수 += 1
    elif is_vip[i] == 1:
        경우의수 *= dp[계수] 
        계수 = 0
'''
# dp 생성
dp = [0] * (n+1)
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]


# vip 표시
is_vip = [0] * (n+1)
for i in range(m):
    is_vip[int(input())] = 1

# 계수, 경우의 수
k = 0
res = 1

# 답 구하기
for i in range(1, n+1):
    # vip가 아니면 계수 증가
    if is_vip[i] == 0:
        k += 1
        # 마지막이 vip 좌석이 아닐 때 계산식 곱해준다
        if i == n:
            res *= dp[k]
    # vip면 경우의 수에 dp[계수] 만큼 증가 시키고 계수 초기화
    elif is_vip[i] == 1:
        if dp[k]:
            res *= dp[k]
        k = 0


print(res)