def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = []
    for _ in range(n):
        w, h = map(int, input().split())
        arr.append((w, h))

    ans = []
    for info in arr:
        mid = 1
        for compare in arr:
            if info[0] < compare[0] and info[1] < compare[1]:
                mid += 1
        ans.append(mid)
    print(*ans)


if __name__ == "__main__":
    main()