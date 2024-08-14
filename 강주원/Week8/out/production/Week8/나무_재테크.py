import sys, copy
input = sys.stdin.readline

# n = 밭의 크기 n*n, m = 나무의 개수, k = 재배년수
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
field = copy.deepcopy(a)
# M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.
trees = [list(map(int, input().split())) for _ in range(m)]
dead_trees = []
# 나이순 정렬
trees.sort(key=lambda x:x[2])
'''
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
'''
def spring():
    for i in range(len(trees)):
        tree = trees[i]
        r, c, age = tree
        if r == -1 and c == -1:
            continue
        r -= 1
        c -= 1
        if field[r][c] >= age:
            field[r][c] -= age
            tree[2] += 1
        else:
            dead_trees.append([r+1, c+1, age])
    
    for tree in dead_trees:
        trees.remove(tree)


'''
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
'''
def summer():
    for tree in dead_trees:
        r, c, age, idx = tree
        if r != -1 and c != -1:
            continue
        r -= 1
        c -= 1
        field[r][c] += age//2


'''
가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
'''
def fall():
    for tree in trees:
        r, c, age = tree
        if r == -1 and c == -1:
            continue
        r -= 1
        c -= 1
        for dir in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
            new_r = dir[0]
            new_c = dir[1]
            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= n:
                continue
            trees.insert(0, [new_r+1, new_c+1, 1])
    


'''
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 a[r][c]이고, 입력으로 주어진다.
'''
def winter():
    for i in range(n):
        for j in range(n):
            field[i][j] += a[i][j]
        


for i in range(k):
    spring()
    summer()
    fall()
    winter()

res = 0
for tree in trees:
    r, c, age = tree
    if r == -1 and c == -1:
        continue
    res += 1

print(res)