def main():
    import sys
    input = sys.stdin.readline

    m, n, h = map(int, input().split())
    board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    ready = 0
    tomatos = []

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    ready += 1
                elif board[i][j][k] == 1:
                    tomatos.append((i, j, k, 0))

    print(tomatos, ready)

if __name__ == "__main__":
    main()