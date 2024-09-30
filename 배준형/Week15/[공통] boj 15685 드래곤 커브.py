import sys
input_ = sys.stdin.readline
import copy

def minput(): return map(int, input_().split())

def solution():
    N = int(input_())
    answer = 0
    graph = [[0]*101 for _ in range(101)]
    # graph = [[0]*11 for _ in range(11)]

    for i in range(N):
        # 드래곤 커브 정보
        x, y, d, g = minput()

        # 드래곤 커브 정보 저장
        save_points(y, x, graph, g, d)
        # print(graph)

    # 정사각형 개수 구하기
    for i in range(100):
    # for i in range(10):
        for j in range(100):
        # for j in range(10):
            if is_square(i, j, graph):
                answer += 1

    # print(graph)

    print(answer)

def save_points(a, b, graph, gen, d):
    dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    stack = [[a, b, -1], [a+dirs[d][0], b+dirs[d][1], d]]
    graph[a][b] = 1
    graph[a+dirs[d][0]][b+dirs[d][1]] = 1

    for _ in range(gen):
        # print(stack)
        tmp_k = len(stack)
        ax, ay = stack[tmp_k-1][0], stack[tmp_k-1][1] 
        for now in range(tmp_k-1, 0, -1):
            sx, sy, ad = stack[now]
            d = -1
            if ad == 1: d = 2
            elif ad == 2: d = 3
            elif ad == 3: d = 0
            elif ad == 0: d = 1
            stack.append([ax+dirs[d][0], ay+dirs[d][1], d])
            graph[ax+dirs[d][0]][ay+dirs[d][1]] = 1
            ax, ay = ax+dirs[d][0], ay+dirs[d][1]


def is_square(a, b, graph):
    if graph[a][b] and graph[a+1][b]\
    and graph[a][b+1] and graph[a+1][b+1]:
        return True

    return False

solution()
