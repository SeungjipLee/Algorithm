def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    Q = deque([1])
    visited = [0] * (n + 1)
    memo = [0] * (n + 1)
    visited[1] = 1
    while Q:
        now = Q.popleft()
        for nxt in adj[now]:
            if visited[nxt] == 0:
                Q.append(nxt)
                memo[nxt] = now
                visited[nxt] = 1

    print(memo)

    for i in range(2, n + 1):
        print(memo[i])


if __name__ == '__main__':
    main()