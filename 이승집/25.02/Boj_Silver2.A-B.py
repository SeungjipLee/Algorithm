import sys
from collections import deque

def main():
    input = sys.stdin.readline

    A, B = map(int, input().split())
    answer = -1
    Q = deque([(A, 1)])

    while Q:
        now, cnt = Q.popleft()
        if now == B:
            answer = cnt
            break
        elif now > B:
            continue

        else:
            Q.append((now * 2, cnt + 1))
            Q.append((now * 10 + 1, cnt + 1))

    print(answer)


if __name__ == "__main__":
    main()