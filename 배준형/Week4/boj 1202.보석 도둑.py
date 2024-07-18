# 풀이가
# 가치가 큰 것 부터 해당 무게를 넣을 수 있는 가방 중에 제일 작은 가방에 넣기
# 가치가 큰 것부터 시작
# 가방을 이진탐색
# 넣을 수 있는 가방이 없으면 넘어가기
# 넣을 수 있는 가방이 있다면 넣고 가방 삭제
# 아니 물건 300,000 개 돌면서
# log(2)300,000 하면 대충 18
# 5,400,000 밖에 안됨
# 하면 시간초과남.
# 삭제에서 시간이 많이 걸리나? 삭제가 최대 N^N 나버리는건가
# 가방을 이중연결리스트로 인덱스 저장하고 삽입삭제를 상수시간에 하면되려나
# 시간 초과
# 삽입 삭제 검색을 logN 으로 끝내고 싶다면
# 균형이진탐색트리를 이용 AVL 트리 혹은 레드블랙트리로 구현됨
# import heapq

class AVLNode:
    # AVL Node 구성요소 키, 높이, 왼, 오
    def __init__(self, key, height=0, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, y):
            if not y or not y.left:
                return y
            x = y.left
            T2 = x.right

            x.right = y
            y.left = T2

            self.update_height(y)
            self.update_height(x)

            return x

    def rotate_left(self, x):
        if not x or not x.right:
            return x
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y
    
    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        
        # 삽입했으면 균형 맞추기
        self.update_height(node)
        balance = self.get_balance(node)
        
        # balance = height(node.left) - height(node.right)
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # 해당 노드가 삭제하고자 하는 것일 때
            # return 해주는 것은 얘가 root가 될 애라고 알려주는 것
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # 현재 노드를 삭제하면 자기보다 바로 다음 큰 수를 현재 노드 자리에 위치시키기
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
            
        self.update_height(node)
        
        balance = self.get_balance(node)
        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        # print("delete", node.key)
        return node
        
    
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    
    def find_successor(self, node, key):
        successor = None
        while node:
            if key <= node.key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor
     
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(node.key, end=" ")
        self.in_order(node.right)     

N, K = map(int, input().split()) # N : 보석 수, K : 가방 수 1 ~ 300,000
items = [] # 보석 리스트
bags = AVLTree() # 가방 리스트, 각 가방에는 최대 한 개의 보석만 넣을 수 있다.
root = None

for _ in range(N):
    M, V = map(int, input().split()) # M : 무게, V : 가치 0 ~ 1,000,000
    items.append([M, V])

for _ in range(K):
    root = bags.insert(root, int(input()))

# bags.in_order(root)
# print()
# print(root.key)
items.sort(reverse=True, key=lambda x: x[1])
# print(items)
answer = 0

for item in items:
    if root is None:
        break
    bag = bags.find_successor(root, item[0])
    
    if bag is not None:
        # print(bag.key)
        answer += item[1]
        root = bags.delete(root, bag.key)    

print(answer)

# 시간초과
# import bisect
# N, K = map(int, input().split()) # N : 보석 수, K : 가방 수 1 ~ 300,000
# items = [] # 보석 리스트
# bags = [] # 가방 리스트, 각 가방에는 최대 한 개의 보석만 넣을 수 있다.

# for _ in range(N):
#     M, V = map(int, input().split()) # M : 무게, V : 가치 0 ~ 1,000,000
#     items.append([M, V, 0, 0])

# for _ in range(K):
#     C = int(input()) # C : 가방의 최대 무게 0 ~ 100,000,000
#     bags.append(C)

# items.sort(reverse=True, key=lambda x: x[1])
# items.sort(key=lambda x: x[0])
# for i in range(N):
#     items[i][3] = i
# bags.sort()

# def lower_bound(a, x, s, e):
#     while s < e:
#         mid = (s+e)//2
#         if a[mid][0] < x: s = mid+1
#         else: e = mid
#     return s

# answer = 0
# for bag in bags:
#     # 가방에는 담을 수 있는 보석 중 최대 무게 반환
#     idx = lower_bound(items, bag, 0, N)
#     # print(idx)
#     goal = sorted(items[:idx], key=lambda x : (x[1], -x[2]), reverse=True)
#     # print(goal)
#     # print(items)
#     if goal:
#         goal = goal[0]
#         items[goal[3]][2] = 1
#         answer += items[goal[3]][1]

# print(answer)
# 2 3 4

# 3  6  
# 2  3
# 3  2,4
