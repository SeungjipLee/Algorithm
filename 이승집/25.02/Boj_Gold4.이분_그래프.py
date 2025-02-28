import sys
from collections import deque


def is_bipartite(v, adj):
    color = [-1] * (v + 1)

    for start in range(1, v + 1):
        if color[start] != -1:
            continue

        Q = deque([start])
        color[start] = 0

        while Q:
            now = Q.popleft()
            for nxt in adj[now]:
                if color[nxt] == -1:
                    color[nxt] = 1 - color[now]
                    Q.append(nxt)
                elif color[nxt] == color[now]:
                    return "NO"

    return "YES"


def main():
    input = sys.stdin.readline
    tc = int(input())
    for _ in range(tc):
        v, e = map(int, input().split())
        adj = {i: [] for i in range(1, v + 1)}

        for _ in range(e):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        print(is_bipartite(v, adj))


if __name__ == "__main__":
    main()

"""input
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
"""