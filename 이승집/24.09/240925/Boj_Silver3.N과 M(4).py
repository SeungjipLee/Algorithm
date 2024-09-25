N, M = map(int, input().split())

arr = []


def btc():
    global N, M
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if arr and arr[-1] > i:
            continue
        arr.append(i)
        btc()
        arr.pop()


btc()