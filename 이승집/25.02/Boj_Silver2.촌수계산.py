def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    r1, r2 = map(int, input().split())
    m = int(input())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (n + 1)
    visited[r1] = 1
    stack = [(r1, 0)]
    ans = -1

    while stack:
        now, acc = stack.pop()
        if now == r2:
            ans = acc
            break

        for nxt in adj[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append((nxt, acc + 1))

    print(ans)


if __name__ == '__main__':
    main()

"""input
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""