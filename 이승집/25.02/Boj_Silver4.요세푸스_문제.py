def main():
    n, m = map(int, input().split())

    arr = list(range(1, n + 1))
    idx = 0
    print("<", end="")
    while n != 1:
        idx = (idx + m - 1) % n
        print(arr.pop(idx), end=", ")
        n -= 1

    print(f"{arr[0]}>")


if __name__ == '__main__':
    main()