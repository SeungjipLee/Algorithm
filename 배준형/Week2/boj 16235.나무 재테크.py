import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

# field : 가장 처음에 모든 칸에 5만큼 양분이 들어 있다.
field = [[5] * n for _ in range(n)]
# graph : 겨울에 각 칸마다 추가되는 양분 
graph = [list(map(int, input().split())) for _ in range(n)]
# trees : 각 칸마다 몇 살의 나무가 몇 그루 있는지
trees = [[[] for _ in range(n)] for _ in range(n)]
# is_tree : 해당 배열에는 나무가 있는 좌표 정보만 [x, y]로 저장됨
is_tree = []

for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    is_tree.append([x, y])
    heapq.heappush(trees[x][y], [z, 1])

for _ in range(k):
    # print("############### this is year of ", _)
    # print(field)
    # print(trees)
    # 여름에 양분이 될 친구들
    stack = []
    # 다음 해에 is_tree에 들어갈 친구들
    stack2 = []
    
    # 봄
    while is_tree:
        x, y = is_tree.pop()
        while trees[x][y]:
            z, cnt = heapq.heappop(trees[x][y])
            new = 0
            while field[x][y] >= z:
                if cnt == 0:
                    break
                # print(x, y, "location ", z+1, "age tree is added")
                cnt -= 1
                field[x][y] -= z
                new += 1
            if new:
                stack2.append([x, y, z+1, new])
            if cnt:
                stack.append([x, y, z, cnt])
                
    # print("stack ", stack)
    # 여름
    while stack:
        x, y, z, cnt = stack.pop()
        field[x][y] += (z // 2) * cnt
        # print(x, y, "palce", z, "old tree is dead", cnt)
    
    # print("stack2", stack2)
    # 가을
    while stack2:
        x, y, z, cnt = stack2.pop()
        is_tree.append([x, y])
        heapq.heappush(trees[x][y], [z, cnt])
        
        if z % 5 == 0:
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                            [1, -1], [1, 0], [1, 1], [0, 1]]:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if trees[nx][ny] and trees[nx][ny][0][0] == 1:
                    # print("same place namu added")
                    trees[nx][ny][0] = [1, trees[nx][ny][0][1] + cnt]
                    # print(nx, ny, trees[nx][ny])
                else:
                    heapq.heappush(trees[nx][ny], [1, cnt])        
                if [nx, ny] not in is_tree:
                    is_tree.append([nx, ny])
    # 겨울
    for i in range(n):
        for j in range(n):
            field[i][j] += graph[i][j]
            
    # print(_, "\n", is_tree, "\n", trees)
            
            
remain = 0            
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            for tree in trees[i][j]:
                # print(i, j, tree)
                remain += tree[1]

print(remain)
# print(field)