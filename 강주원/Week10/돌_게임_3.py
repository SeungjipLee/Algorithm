'''
s는 선공의 승리
c는 후공의 승리입니다
선
후
선
선
후
선
후
선
선
10 후
11 선
12 후
13 선
14 선

1 s
2 c
3 s
4 s
5 s
6 s
7 c
8 s
9 s
10 c
이전 3개가 모두 s면 c?
'''
n = int(input())
dp = [0] * (n+2)
dp[2] = 1
for i in range(5, n+1):
    if dp[i-1] == dp[i-3] == dp[i-4]:
        dp[i] = dp[i-1] == False


if dp[n]:
    print('CY')
else:
    print('SK')
