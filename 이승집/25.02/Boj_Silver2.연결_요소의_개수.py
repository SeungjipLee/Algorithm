ans = 0

def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    visited = [0] * (n + 1)

    def dfs(n):
        global ans
        stack = [n]
        visited[n] = 1
        while stack:
            now = stack.pop()
            for nxt in adj[now]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    stack.append(nxt)
        ans += 1

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)

    print(ans)

if __name__ == "__main__":
    main()