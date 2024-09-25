N, M = map(int, input().split())

arr = []


def backtracking():
    global N, M
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        arr.append(i)
        backtracking()
        arr.pop()


backtracking()