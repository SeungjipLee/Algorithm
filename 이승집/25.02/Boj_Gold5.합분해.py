import sys


def main():
    input = sys.stdin.readline
    mod = 1_000_000_000  # 문제에서 요구하는 나머지

    n, k = map(int, input().split())

    # dp[i][j] = 정수 j개를 사용하여 합이 i가 되는 경우의 수
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # 초기값 설정
    for j in range(1, k + 1):
        dp[0][j] = 1  # 합이 0이면 (모두 0) 1가지
    for i in range(n + 1):
        dp[i][1] = 1  # 정수 1개로 합이 i인 경우는 (i) 한 가지뿐

    # 점화식 적용
    for i in range(1, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod

    print(dp[n][k])


if __name__ == "__main__":
    main()
