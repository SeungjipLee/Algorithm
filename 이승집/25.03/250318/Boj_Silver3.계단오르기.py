import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    if n == 1:
        print(arr[0])
        return
    elif n == 2:
        print(arr[0] + arr[1])
        return

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(dp[-1])


if __name__ == "__main__":
    main()