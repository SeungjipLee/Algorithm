def main():
    import sys
    from itertools import combinations

    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    house = []
    chicken = []
    ans = int(10e9)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append((i, j))
            elif board[i][j] == 2:
                chicken.append((i, j))

    l = len(chicken)
    for i in combinations(range(l), m):
        selected = [chicken[j] for j in i]
        mid = 0
        for home in house:
            min_distance = int(10e9)
            for c in selected:
                distance = abs(c[0] - home[0]) + abs(c[1] - home[1])
                min_distance = min(distance, min_distance)
            mid += min_distance
        ans = min(ans, mid)

    print(ans)


if __name__ == '__main__':
    main()