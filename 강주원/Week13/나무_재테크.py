from collections import deque
import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
field = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]


for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

def spring():
    for i in range(n):
        for j in range(n):
            l = len(trees[i][j])
            for k in range(l):
                if field[i][j] >= trees[i][j][k]:
                    field[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, l):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
    
    return dead_trees
    

def summer(dead_trees):
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                field[i][j] += dead_trees[i][j].pop() // 2


def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            trees[nr][nc].appendleft(1)
            
            field[i][j] += a[i][j]
    


for _ in range(k):
    dead_trees = spring()
    summer(dead_trees)
    fall_winter()


res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])

print(res)
