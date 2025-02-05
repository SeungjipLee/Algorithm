"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    n = int(input())
    Q = deque([])

    for _ in range(n):
        do = input().split()
        if do[0] == "push_front":
            Q.insert(0, int(do[1]))
        elif do[0] == "push_back":
            Q.append(int(do[1]))
        elif do[0] == "pop_front":
            if Q:
                print(Q.popleft())
            else:
                print(-1)
        elif do[0] == "pop_back":
            if Q:
                print(Q.pop())
            else:
                print(-1)
        elif do[0] == "size":
            print(len(Q))
        elif do[0] == "empty":
            if Q:
                print(0)
            else:
                print(1)
        elif do[0] == "front":
            if Q:
                print(Q[0])
            else:
                print(-1)
        elif do[0] == "back":
            if Q:
                print(Q[-1])
            else:
                print(-1)


if __name__ == '__main__':
    main()