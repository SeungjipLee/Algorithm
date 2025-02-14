def main():
    tc = int(input())
    ans = []
    memo = [0, 1, 1, 1, 2, 2]

    for _ in range(tc):
        ans.append(int(input()))

    m = max(ans)

    while len(memo) <= m:
        memo.append(memo[-1] + memo[-5])

    for i in ans:
        print(memo[i])


if __name__ == "__main__":
    main()


"""input
2
6
12
"""